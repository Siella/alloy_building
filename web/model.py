import pandas as pd
import os.path
from sklearn.impute import SimpleImputer, KNNImputer
import numpy as np
import sys
import parameters
import json
import modelling.utils.preds_pipeline as preds_pipeline
import cleaning


def process_dataframe(df, task):
    df = cleaning.cleaning(df)
    return preds_pipeline.make_predictions(df)


def process_single(params):
    d = dict()
    for group in parameters.PARAMETERS.values():
        for elem in group:
            name = elem["name"]
            key = elem["key"]
            if key in params:
                try:
                    d[name] = [float(params[key])]
                except ValueError:
                    pass
            else:
                d[name] = None

    df = pd.DataFrame.from_dict(d)
    result = process_dataframe(df)
    df.insert(len(df.columns), "result", result)
    return {"table": json.loads(df.to_json(orient='split')), "targets": preds_pipeline.TARGETS}


def process_batch(file, options):
    df = pd.read_csv(file, sep=options.get('batchCsvDelimiter', ','), decimal=options.get('batchCsvDecimal', '.'))
    task = options.get("batchTask", "slag")

    result = process_dataframe(df, task)
    for col in result.columns:
        df[col] = result[col]
    return {"table": json.loads(df.to_json(orient='split')), "targets": preds_pipeline.TARGETS}

###########################################################################


COLUMNS_TO_DROP = ['химсталь последний P',
                   'химсталь последний Si',
                   'химсталь последний Cr',
                   'химсталь последний Al',
                   'химсталь последний Cu',
                   'химсталь последний Mo',
                   'химсталь последний Ni',
                   'расход C пров.',
                   'химшлак последний FeO',
                   'химсталь последний N',
                   'ферспл FeV азот.',
                   'химшлак последний MgO',
                   'ферспл  ферванит',
                   'химсталь последний V',
                   'сыпуч  кокс. мелочь (сух.)',
                   'ферспл  Ni H1 пласт.',
                   'расход газ  N2',
                   'химсталь последний C',
                   'сыпуч кварцит',
                   'химсталь последний Ca',
                   'химшлак последний MnO',
                   'химсталь последний S',
                   'ферспл FeSi-75',
                   'N2 (интенс.)',
                   'химсталь последний Ti',
                   'ферспл FeMo',
                   'химсталь последний Mn',
                   'произв  количество плавок',
                   'произв количество плавок (цел)',
                   ]


def filter_table(df):
    df.drop(df[df["МАРКА"] != "Э76ХФ"].index, axis=0, inplace=True)
    df.drop(["МАРКА", "DT"], axis=1, inplace=True)

    row_nan_per = df.isnull().sum(axis=1) / df.shape[1]
    df.drop(row_nan_per[row_nan_per >= 0.3].index, axis=0, inplace=True)

    df.drop(COLUMNS_TO_DROP, axis=1, inplace=True)

    df.drop(df[df['ПРОФИЛЬ'] != 'Р65'].index, axis=0, inplace=True)
    df.drop('ПРОФИЛЬ', axis=1, inplace=True)

    return df


def remove_outliers(df, features=[], left_q=.05, right_q=.95):
    outliers_ids = []
    for f in features:
        x = df[f].dropna()
        x = (x - x.mean()) / x.std()
        outliers_ids += list(x[~x.between(x.quantile(left_q), x.quantile(right_q))].index)
    return list(set(outliers_ids))


def simple_impute(df, col, strategy):
    imputer = SimpleImputer(missing_values=np.nan, strategy=strategy)
    imp_col = imputer.fit_transform(df[col].to_numpy().reshape(-1, 1))
    df[col] = imp_col


def knn_impute(df, col):
    imputer = KNNImputer(n_neighbors=2)
    imp_col = imputer.fit_transform(df[col].to_numpy().reshape(-1, 1))
    imp_col = [item[0] for item in imp_col.tolist()]
    df[col] = imp_col


def simple_impute_wrapper(strategy):
    def func(*args):
        return simple_impute(*args, strategy=strategy)
    return func


IMPUTE_METHODS = {
    "mean": {"callback": simple_impute_wrapper("mean"), "label": "Среднее значение"},
    "median": {"callback": simple_impute_wrapper("median"), "label": "Медианное значение"},
    "most_freq": {"callback": simple_impute_wrapper("most_frequent"), "label": "Мода"},
    "knn": {"callback": knn_impute, "label": "kNN"},
}

def process(file, options):
    ext = os.path.splitext(file.filename)[1][1:].lower()
    if ext == 'csv':
        data = pd.read_csv(file.stream, sep=';', decimal=',', index_col=0, parse_dates=["DT"])
    else:
        data = pd.read_excel(file.stream)

    data.set_index('nplv')
    data = filter_table(data)

    targets = ['химшлак последний Al2O3', 'химшлак последний CaO', 'химшлак последний R', 'химшлак последний SiO2']
    numerical_columns = data.select_dtypes(exclude=['category', 'object', 'datetime64']).columns.tolist()

    if options.get('removeOutliers', False):
        outlier_ids = remove_outliers(data, numerical_columns, .001, .999)
        data.drop(set(outlier_ids), axis=0, inplace=True)

    impute_method = IMPUTE_METHODS.get(options.get('imputeMethod', 'knn'), knn_impute)["callback"]
    cols = set(data.columns) - set(targets)
    nan_cols = [col for col in cols if data[col].isnull().values.any()]
    for col in nan_cols:
        impute_method(data, col)

    keys = data.keys()

    return list(keys)
