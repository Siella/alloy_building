import numpy as np
from sklearn.impute import KNNImputer


def get_pop_steel_grad(df):
    pop_grade = df.groupby('МАРКА')[['произв количество плавок (цел)']].agg(sum).idxmax().values[0]
    return pop_grade


def nul_cols(df_in):
    nuls = df_in.isnull().mean().to_frame().sort_values(by=0, ascending=False)
    nuls.columns = ['%_nuls']
    cols2drop = nuls.loc[nuls['%_nuls'] > 0.5].index
    return cols2drop


def remove_outliers(df, features=[], left_q=.05, right_q=.95):
    outliers_ids = []
    for f in features:
        x = df[f].dropna()
        x = (x - x.mean()) / x.std()
        outliers_ids += list(x[~x.between(x.quantile(left_q), x.quantile(right_q))].index)
    return list(set(outliers_ids))


def remove_extraoutliers(df, features=[]):
    x = df[features].copy()
    # standardize features
    for col in x.columns:
        x[col] = (x[col] - x[col].mean()) / x[col].std()
    return x[(x >= 5).any(1)].index.tolist()


def find_ordinal_with_dominant(df, size=50, with_dominant_value=False, max_percent=0.9):
    # if a number of unique varibles is less than or equal to n, this variable is considered as categorial
    names = df.columns
    ordinal_vars = []
    for n in names:
        if df[n].nunique() <= size:
            if with_dominant_value:
                nums = df[n].value_counts().values
                if (len(nums) > 0) and (nums[0] / np.sum(nums) > max_percent):
                    ordinal_vars.append(n)
            else:
                ordinal_vars.append(n)

    return ordinal_vars


def knn_impute(df, col):
    imputer = KNNImputer(n_neighbors=2)
    imp_col = imputer.fit_transform(df[col].to_numpy().reshape(-1, 1))
    imp_col = [item[0] for item in imp_col.tolist()]
    df[col] = imp_col


def cleaning(df_in, outliers_min=0, outliers_max=1):
    NOT_DROP = set(['ферспл CaC2', 'произв количество обработок'])
    TARGETS = ['химшлак последний Al2O3', 'химшлак последний CaO',
               'химшлак последний R', 'химшлак последний SiO2']

    if "МАРКА" in df_in.columns:
        df = df_in[df_in['МАРКА'] == get_pop_steel_grad(df_in)]
    else:
        df = df_in

    cols2drop = nul_cols(df)
    df.drop(cols2drop, axis=1, inplace=True)

    df = df.loc[~df['t под током'].isnull()]

    # Профиль
    if "ПРОФИЛЬ" in df.columns:
        profile_value = df['ПРОФИЛЬ'].value_counts()
        profile = profile_value.index[np.argmax(profile_value.values)]
        df = df[df['ПРОФИЛЬ'] == profile]
        if 'ПРОФИЛЬ' not in NOT_DROP:
            df.drop('ПРОФИЛЬ', axis=1, inplace=True)

    if 'DT' not in NOT_DROP and 'DT' in df.columns:
        df.drop('DT', axis=1, inplace=True)

    # Ординальные
    dominant_ords = find_ordinal_with_dominant(df, with_dominant_value=True, max_percent=0.9)
    df.drop(set(dominant_ords) - NOT_DROP, axis=1, inplace=True)

    # Outliers
    # NUMERICAL = df.select_dtypes(exclude=['category', 'object', 'datetime64']).columns.tolist()
    # outliers_ids = remove_outliers(df, NUMERICAL, outliers_min, outliers_max)
    # extra_outliers = remove_extraoutliers(df, NUMERICAL)
    # df.drop(set(outliers_ids + extra_outliers) - NOT_DROP, axis=0, inplace=True)

    cols = set(df.columns) - set(TARGETS)
    nan_cols = [col for col in cols if df[col].isnull().values.any()]
    # Стратегия knn
    for col in nan_cols:
        knn_impute(df, col)

    return df.reset_index(drop=True)
