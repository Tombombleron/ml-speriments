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

imputer = Imputer()


