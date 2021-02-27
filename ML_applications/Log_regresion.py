# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 11:51:26 2020

@author: jesus
"""
#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
#%%
#pandas wisconsin cancer database with all features selected
cancer = pd.read_csv("datasets\cancer_wisconsin.csv")
cancer = cancer.drop(labels = "id", axis = 1)
#%%
label = cancer[cancer.columns[0]]
features = cancer.drop(labels = "diagnosis", axis = 1)
features = features.drop(labels = "Unnamed: 32", axis = 1)
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(features)

#%%
X_train, X_test, Y_train, Y_test = train_test_split(scaled_features,label, stratify=label, test_size=0.30)



#%%
logisticreg = LogisticRegression(max_iter= 300)
logisticreg.fit(X_train, Y_train)
Y_pred = logisticreg.predict(X_test)


#%%
f1_malign = f1_score(Y_test, Y_pred, pos_label="M",average = "binary")
print(f1_malign)
f1_benign = f1_score(Y_test, Y_pred, pos_label="B",average = "binary")
print(f1_benign)
acc = accuracy_score(Y_test, Y_pred)
print(acc)
rec = recall_score(Y_test, Y_pred, pos_label="M")
print(rec)

