#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 20:47:52 2018

@author: tombombleron
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

def get_mae(X_train, y_train, X_test, y_test, min_samples=2):

  clf = RandomForestRegressor(min_samples_split=min_samples)
  clf.fit(X_train, y_train)
  predictions = clf.predict(X_test)
  mae = mean_absolute_error(y_test, predictions)
  
  return mae

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

train.dropna(axis=0, subset=["SalePrice"], inplace=True)

y = train.SalePrice
X = train.drop("SalePrice", axis=1).select_dtypes(exclude=["object"])

X_train, X_test, y_train, y_test = train_test_split(X.as_matrix(), y.as_matrix(), test_size=0.25)

imputer = Imputer()

X_train = imputer.fit_transform(X_train)
X_test= imputer.fit_transform(X_test)

def calc_xgb(X_train, y_train, X_test, y_test, learning_rate_max=0.05):
  
  alpha_list= []
  mae_list = []

  for alpha in np.arange(0.01, learning_rate_max, 0.005):
    clf = XGBRegressor(n_estimators=1000, learning_rate=alpha)
    clf.fit(X_train, y_train, early_stopping_rounds=5, eval_set=[(X_test, y_test)], verbose=False)
    predictions = clf.predict(X_test)

    alpha_list.append(alpha)
    mae_list.append(mean_absolute_error(y_test, predictions))

  plt.plot(mae_list, alpha_list, 'rx')
  plt.ylabel("alpha value")
  plt.xlabel("MAE value")
  plt.title("Effect of alpha on MAE using xgboost")
  plt.show()
  
  print "The alpha with the lowest MAE is", alpha_list[mae_list.index(min(mae_list))]
  print "The MAE value is", min(mae_list)
  
calc_xgb(X_train, y_train, X_test, y_test, 0.4)

