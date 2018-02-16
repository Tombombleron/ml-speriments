#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 20:47:52 2018

@author: tombombleron
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import mae

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

X_train, X_test, y_train, y_test = train_test_split(train.drop("SalePrice", axis=1), train.SalePrice, random_state=0)

columns = ["LotArea", "LotFrontage", "SaleCondition"]

X_train = X_train[columns]
X_test = X_test[columns]

oneHot_X_train = pd.get_dummies(X_train)
oneHot_X_test = pd.get_dummies(X_test)

my_imputer = Imputer()

imputed_X_train = my_imputer.fit_transform(oneHot_X_train)
imputed_X_test = my_imputer.fit_transform(oneHot_X_test)

clf = RandomForestRegressor()
clf.fit(imputed_X_train, y_train)
predictions = clf.predict(imputed_X_test)

X_train = X_train[columns[:-1]]
X_test = X_test[columns[:-1]]

imputed_X_train = my_imputer.fit_transform(X_train)
imputed_X_test = my_imputer.fit_transform(X_test)

clf1 = RandomForestRegressor()
clf1.fit(imputed_X_train, y_train)
predictions1 = clf1.predict(imputed_X_test)

print "MAE with get_dummies:", round(mean_absolute_error(y_test, predictions), 2)
print "MAE without get dummies:", round(mean_absolute_error(y_test, predictions1), 2)