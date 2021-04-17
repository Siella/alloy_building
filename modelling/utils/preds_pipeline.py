import itertools
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn_pandas import DataFrameMapper, gen_features

TARGETS = ['химшлак последний Al2O3', 'химшлак последний CaO',
           'химшлак последний R', 'химшлак последний SiO2']

MODEL_NAMES = ['Al2O3', 'R', 'SiO2', 'CaO']
MODELS = dict()
for name in MODEL_NAMES:
    MODELS[name] = pickle.load(open('modelling/models/'+name+'.sav', 'rb'))

with open('modelling/utils/cols_for_modelling.txt', encoding='cp1251') as f:
    FEATURES = f.read().splitlines()

with open('modelling/utils/cols_for_engineering.txt', encoding='cp1251') as f:
    pairs = f.read().splitlines()

EXTRA_FEAT = []
for pair in pairs:
    EXTRA_FEAT += [eval(pair)]

class Error(Exception):
    pass

class InputError(Error):
    """Exception raised for errors in the input."""
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def safe_division(x, y):
    if (x != x) | (y != y) | (y == 0):
        return np.nan
    return x / y


def feature_engineering(df):
    df_new = df[FEATURES]
    # ratio
    for pair in EXTRA_FEAT:
        new_col = pair[0]+'_'+pair[1]+'_ratio'
        df_new[new_col] = df.apply(lambda x: safe_division(x[pair[0]],x[pair[1]]), axis=1)
    # substraction
    t_features = ['t вып-обр', 't обработка', 't под током', 't продувка']
    t_combinations = list(itertools.combinations(t_features, 2))
    for pair in t_combinations:
        new_col = pair[0]+'_'+pair[1]+'_sub'
        df_new[new_col] = df.apply(lambda x: abs(x[pair[0]]-x[pair[1]]), axis=1)
    return df_new


def map_features(features=[]):
    numerical_def = gen_features(
        columns=[[c] for c in features],
        classes=[
            {'class': StandardScaler}
        ]
    )
    return numerical_def


def make_predictions(df, *arg, **kwargs):
    df = feature_engineering(df)

    mapper = DataFrameMapper(map_features(df.columns), df_out=True)
    preds_Al2O3 = MODELS['Al2O3'].predict(mapper.fit_transform(df))
    df['химшлак последний Al2O3'] = np.exp(preds_Al2O3) # было log-преобразование 

    # mapper = DataFrameMapper(map_features(df.columns), df_out=True)
    # preds_R = MODELS['R'].predict(mapper.fit_transform(df))
    # df['химшлак последний R'] = np.around(preds_R, 2) # ближе к дискретным значения
    
    mapper = DataFrameMapper(map_features(df.columns), df_out=True)
    preds_R = MODELS['R'].predict(mapper.fit_transform(df))
    df['химшлак последний R'] = np.around(preds_R, 2) # ближе к дискретным значения
    df['химшлак последний R_химшлак последний Al2O3_mul'] = df['химшлак последний Al2O3']*df['химшлак последний R'] # смысловая фича

    mapper = DataFrameMapper(map_features(df.columns), df_out=True)
    print("SiO2:\n", MODELS['SiO2'].coef_)
    preds_SiO2 = MODELS['SiO2'].predict(mapper.fit_transform(df))
    df['химшлак последний SiO2'] = preds_SiO2

    mapper = DataFrameMapper(map_features(df.columns), df_out=True)
    preds_CaO = MODELS['CaO'].predict(mapper.fit_transform(df))
    df['химшлак последний CaO'] = preds_CaO

    return df[TARGETS]