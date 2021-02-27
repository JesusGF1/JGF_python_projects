# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:22:12 2020

@author: jesus
"""
#%%
import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_classif, SelectKBest
from sklearn.model_selection import train_test_split
from ReliefF import ReliefF


#%%
#pandas wisconsin cancer database with all features selected
cancer = pd.read_csv("datasets\cancer_wisconsin.csv")
cancer = cancer.drop(labels = "id", axis = 1)
#%%
label = cancer[cancer.columns[0]]
features = cancer.drop(labels = "diagnosis", axis = 1)
features = features.drop(labels = "Unnamed: 32", axis = 1)
X_train, X_test, Y_train, Y_test = train_test_split(features,label, stratify=label, test_size=0.30,random_state=23)
#%%

#univariate feature selection
selector = SelectKBest(mutual_info_classif, k=5)
selector.fit(X_train, Y_train)
cols = selector.get_support(indices=True) #get support te da la lista de booleanos para encontrar las columnas en el df
X_train_univariate = X_train.iloc[:,cols]
unifeats = X_train_univariate.columns
unifeats = ','.join(unifeats)
print("The selected features with the univariate filter are {}".format(unifeats)) #concave points_mean,radius_worst,perimeter_worst,area_worst,concave points_worst

#%%
#multivariate feature selection
fs = ReliefF(n_neighbors=4, n_features_to_keep=5) #texture_mean,smoothness_mean,compactness_mean,concavity_mean,concave points_se
fs.fit(X_train.to_numpy(), Y_train.to_numpy())
#texture_mean,concave points_mean,area_se,compactness_worst,symmetry_worst

idx = np.where(fs.top_features <5)

columns = list(X_train.columns)

X_train_multi = columns[idx[0][0]] + "," + columns[idx[0][1]] + ","+ columns[idx[0][2]] + ","+ columns[idx[0][3]]+ "," + columns[idx[0][4]] 
#'texture_mean,symmetry_mean,smoothness_se,compactness_se,concave points_se'
multifeats = X_train_multi
print("The selected features with the multivariate filter are {}".format(multifeats))

#%%
#Wrapper method using RFE for logistic regression
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
selector = SelectFromModel(estimator=LogisticRegression(max_iter = 200)).fit(X_train, Y_train)
colindx = selector.get_support(indices=True) #get support te da un array con los indices de los seleccionados
X_train_wrapper = X_train.iloc[:,colindx]
wrapperfeats = X_train_wrapper.columns
wrapperfeats = ','.join(wrapperfeats)
print("The selected features with the wrapper for logReg filter are {}".format(wrapperfeats)) #radius_mean,texture_se,radius_worst,compactness_worst,concavity_worst





