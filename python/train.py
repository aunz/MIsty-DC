import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import VotingClassifier
from xgboost import XGBClassifier

data = pd.read_csv('challenge.csv')

for i in data.select_dtypes('object'): data[i] = data[i].fillna('').str.lower()

y = np.where(data['y'] > 0, 1, 0)

ohe_x2 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
ohe_x2.fit(data['x2'].str[0].values.reshape(-1, 1))

ohe_x4 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
ohe_x4.fit(data['x4'].str[:2].values.reshape(-1, 1))

ohe_x5 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
ohe_x5.fit(data['x5'].values.reshape(-1, 1))

ohe_x8 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
ohe_x8.fit(data['x8'].values.reshape(-1, 1))

ohe_x15 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
ohe_x15.fit(data['x15'].values.reshape(-1, 1))

ohe_x16 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
ohe_x16.fit(data['x16'].values.reshape(-1, 1))

ohe_x17 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
ohe_x17.fit(data['x17'].values.reshape(-1, 1))

ohe_x23 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
ohe_x23.fit(data['x23'].values.reshape(-1, 1))

ohe_x24 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
ohe_x24.fit(data['x24'].str[:2].values.reshape(-1, 1))

ohe_x25 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
ohe_x25.fit(data['x25'].values.reshape(-1, 1))

ohe_x26 = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
tmp = data['x26'].replace(to_replace='.*facebook.*', value='facebook', regex=True)
tmp = tmp.replace(to_replace='.*play games.*', value='play games earn money', regex=True)
ohe_x26.fit(tmp.values.reshape(-1, 1))

params = {
    'colsample_bytree': 0.9492405652889128,
    'gamma': 0.2174707094781907,
    'learning_rate': 0.2087465061696673,
    'max_depth': 4,
    'min_child_weight': 4,
    'reg_alpha': 0.4475446011595685,
    'reg_lambda': 0.16373566452669497,
    'scale_pos_weight': 65.66666666666667,
    'subsample': 0.781163089515965,
    'verbosity': 0,
}


model = VotingClassifier(
    estimators=[
        ('model1', LogisticRegression(random_state=0, solver='lbfgs', max_iter=5000, class_weight='balanced')),
        ('model2', XGBClassifier(n_jobs=-1, random_state=0, **params)),
        ('model3', GaussianNB()),
    ],
#     voting='hard',
#     voting='soft',
    voting='soft', weights=[100, 1, 1]
)

model.fit(X, y)

tmp = model.predict(X)

from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

print(classification_report(y, tmp))
print(confusion_matrix(y, tmp))
print(roc_auc_score(y, model.predict_proba(X)[:,1]))

# save things

import pickle

with open('model.pkl', 'wb') as f: pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x2.pkl', 'wb') as f: pickle.dump(ohe_x2, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x4.pkl', 'wb') as f: pickle.dump(ohe_x4, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x5.pkl', 'wb') as f: pickle.dump(ohe_x5, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x8.pkl', 'wb') as f: pickle.dump(ohe_x8, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x15.pkl', 'wb') as f: pickle.dump(ohe_x15, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x16.pkl', 'wb') as f: pickle.dump(ohe_x16, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x17.pkl', 'wb') as f: pickle.dump(ohe_x17, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x23.pkl', 'wb') as f: pickle.dump(ohe_x23, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x24.pkl', 'wb') as f: pickle.dump(ohe_x24, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x25.pkl', 'wb') as f: pickle.dump(ohe_x25, f, protocol=pickle.HIGHEST_PROTOCOL)
with open('ohe_x26.pkl', 'wb') as f: pickle.dump(ohe_x26, f, protocol=pickle.HIGHEST_PROTOCOL)
