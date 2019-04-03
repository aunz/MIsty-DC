import numpy as np
import pandas as pd

# from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# from sklearn.linear_model import LogisticRegression
# from sklearn.naive_bayes import GaussianNB
# from sklearn.ensemble import VotingClassifier
# from xgboost import XGBClassifier

import pickle

with open('model.pkl', 'rb') as f: model = pickle.load(f)
with open('ohe_x2.pkl', 'rb') as f: ohe_x2 = pickle.load(f)
with open('ohe_x4.pkl', 'rb') as f: ohe_x4 = pickle.load(f)
with open('ohe_x5.pkl', 'rb') as f: ohe_x5 = pickle.load(f)
with open('ohe_x8.pkl', 'rb') as f: ohe_x8 = pickle.load(f)
with open('ohe_x15.pkl', 'rb') as f: ohe_x15 = pickle.load(f)
with open('ohe_x16.pkl', 'rb') as f: ohe_x16 = pickle.load(f)
with open('ohe_x17.pkl', 'rb') as f: ohe_x17 = pickle.load(f)
with open('ohe_x23.pkl', 'rb') as f: ohe_x23 = pickle.load(f)
with open('ohe_x24.pkl', 'rb') as f: ohe_x24 = pickle.load(f)
with open('ohe_x25.pkl', 'rb') as f: ohe_x25 = pickle.load(f)
with open('ohe_x26.pkl', 'rb') as f: ohe_x26 = pickle.load(f)

    
def processData(df):
    for i in df.select_dtypes('object').columns: df[i] = df[i].fillna('').str.lower()
    X = df[['x7', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x18', 'x19', 'x20', 'x21', 'x22']].copy()
    for i in X.columns: X[i] = X[i].astype(float)
    X['x7'] = X['x7'] / 100
    X['x14'] = X['x14'] / 1000
    
    x2 = ohe_x2.transform(df['x2'].str[0].values.reshape(-1, 1))[:, [2, 3, 4, 5]]
    x4 = ohe_x4.transform(df['x4'].str[:2].values.reshape(-1, 1))[:, [34, 12,  3, 11, 31, 30, 10,  1, 25,  6]]
    x5 = ohe_x5.transform(df['x5'].values.reshape(-1, 1))[:, [2, 1, 0]]
    x8 = ohe_x8.transform(df['x8'].values.reshape(-1, 1))[:, [3, 2, 1, 0]]
    x15 = ohe_x15.transform(df['x15'].values.reshape(-1, 1))[:, [86,  58,  45,  67, 114,  72,  37,  89,  73,  91]]
    x16 = ohe_x16.transform(df['x16'].values.reshape(-1, 1))[:, [1, 0]]
    x17 = ohe_x17.transform(df['x17'].values.reshape(-1, 1))[:, [4, 3, 2, 5, 1, 0]]
    x23 = ohe_x23.transform(df['x23'].values.reshape(-1, 1))[:, [2, 1]]
    x24 = ohe_x24.transform(df['x24'].str[:2].values.reshape(-1, 1))[:, [29,  0, 23, 24, 22, 15, 17,  2, 12, 25]]
    x25 = ohe_x25.transform(df['x25'].values.reshape(-1, 1))[:, [119,  76,   0,  77, 123, 344, 133, 128, 295, 278]]
    tmp = df['x26'].replace(to_replace='.*facebook.*', value='facebook', regex=True)
    tmp = tmp.replace(to_replace='.*play games.*', value='play games earn money', regex=True)
    x26 = ohe_x26.transform(tmp.values.reshape(-1, 1))[:, [10,  0, 21, 12, 17, 14,  1,  7, 15, 13]]
    X = np.hstack((X.values, x2, x4, x5, x8, x15, x16, x17, x23, x24, x25, x26))
    
    return X

########################
# test if it's working #

data = pd.read_csv('challenge.csv')
y = np.where(data['y'] > 0, 1, 0)

X = processData(data)

tmp = model.predict(X)

print(classification_report(y, tmp))
print(confusion_matrix(y, tmp))
print(roc_auc_score(y, model.predict_proba(X)[:,1]))

del data, y, X, tmp, f, pickle, classification_report, confusion_matrix, roc_auc_score

#######################