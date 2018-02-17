#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:13:47 2018

@author: tombombleron
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

le = LabelEncoder()

data = pd.read_csv("iris.csv", header=None)
X = data.drop(4, axis=1)
y = data[4]
le.fit(y)
y = le.transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

clf = XGBRegressor(n_estimators=1000, learning_rate=0.045)
clf.fit(X_train, y_train, early_stopping_rounds=5, eval_set=[(X_test, y_test)], verbose=False)
predictions = clf.predict(X_test)
rounded_predictions = [int(round(x)) for x in predictions]
compare = zip(y_test, rounded_predictions)

print "MAE:", mean_absolute_error(y_test, rounded_predictions)
print "MSE:", mean_squared_error(y_test, rounded_predictions)
print compare

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
  
#calc_xgb(X_train, y_train, X_test, y_test)