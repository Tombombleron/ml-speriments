#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:36:01 2018

@author: tombombleron
"""

import sys
import pandas as pd
import numpy as np
import scipy as sp
import IPython
import sklearn
import random
import time
import warnings
warnings.filterwarnings("ignore")

# Common Model Algos
from sklearn import svm, tree, linear_model, neighbors, naive_bayes, ensemble, discriminant_analysis, gaussian_process
from xgboost import XGBRegressor

# Common Model Helpers
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn import feature_selection
from sklearn import model_selection
from sklearn import metrics

# Visuals
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns
from pandas.tools.plotting import scatter_matrix

# Set Default Params
mpl.style.use('ggplot')
sns.set_style('white')
pylab.rcParams['figure.figsize'] = 12,8

data_raw = pd.read_csv("Data/train.csv")
data_val = pd.read_csv("Data/test.csv")

data1 = data_raw.copy(deep=True)

data_cleaner = [data1, data_val]

print("Train columns with null values:\n", data1.isnull().sum())
print("-"*25)
print("Test columns with null values:\n", data_val.isnull().sum())
print("-"*25)
print(data_raw.describe(include="all"))
print("-"*25)

for dataset in data_cleaner:
    
    dataset["Age"].fillna(dataset["Age"].median(), inplace=True)
    dataset["Embarked"].fillna(dataset["Embarked"].mode()[0], inplace=True)
    dataset["Fare"].fillna(dataset["Fare"].median(), inplace=True)
    
drop_cols = ["PassengerId", "Cabin", "Ticket"]
data1.drop(drop_cols, axis=1, inplace=True)

print(data1.isnull().sum())
print("-"*25)
print(data_val.isnull().sum())
print("-"*25)

for dataset in data_cleaner:
    
    dataset["FamilySize"] = dataset["SibSp"] + dataset["Parch"] + 1
    dataset["IsAlone"] = 1
    dataset["IsAlone"].loc[dataset["FamilySize"] > 1] =0
    dataset["Title"] = dataset["Name"].str.split(", ", expand=True)[1].str.split(".", expand=True)[0]
    dataset["FareBin"] = pd.qcut(dataset['Fare'], 4)
    dataset["AgeBin"] = pd.cut(dataset["Age"].astype(int), 5)

stat_min = 10
title_names = (data1["Title"].value_counts() < stat_min)
data1["Title"] = data1["Title"].apply(lambda x: "Misc" if title_names.loc[x] == True else x)
print(data1["Title"].value_counts())
print("-"*25)

print(data1.info())
print(data_val.info())
print(data1.sample(10))

label = LabelEncoder()

for dataset in data_cleaner:
    
    dataset["Sex_Code"] = label.fit_transform(dataset["Sex"])
    dataset["Embarked_Code"] = label.fit_transform(dataset["Embarked"])
    dataset["Title_Code"] = label.fit_transform(dataset["Title"])
    dataset["AgeBin_Code"] = label.fit_transform(dataset["AgeBin"])
    dataset["FareBin_Code"] = label.fit_transform(dataset["FareBin"])

Target = ["Survived"]

data1_x = ['Sex','Pclass', 'Embarked', 'Title','SibSp', 'Parch', 'Age', 'Fare', 'FamilySize', 'IsAlone'] #pretty name/values for charts
data1_x_calc = ['Sex_Code','Pclass', 'Embarked_Code', 'Title_Code','SibSp', 'Parch', 'Age', 'Fare'] #coded for algorithm calculation
data1_xy =  Target + data1_x
print('Original X Y: ', data1_xy, '\n')

data1_x_bin = ['Sex_Code','Pclass', 'Embarked_Code', 'Title_Code', 'FamilySize', 'AgeBin_Code', 'FareBin_Code']
data1_xy_bin = Target + data1_x_bin
print('Bin X Y: ', data1_xy_bin, '\n')

data1_dummy = pd.get_dummies(data1[data1_x])
data1_x_dummy = data1.columns.tolist()
data1_xy_dummy = Target + data1_x_dummy
print("Dummy X Y: ", data1_xy_dummy, "\n")

print(data1.isnull().sum())
print("-"*25)
print(data1.info())
print("-"*25)
print(data_val.isnull().sum())
print("-"*25)
print(data1.info())
print("-"*25)
print(data_raw.describe(include="all"))
print("-"*25)

train1_X, test1_X, train1_Y, test1_Y = model_selection.train_test_split(data1[data1_x_calc],
                                                                        data1[Target],
                                                                        random_state=0
                                                                        )
train1_X_bin, test1_X_bin, train1_Y_bin, test1_y_bin = model_selection.train_test_split(data1[data1_x_bin],
                                                                                        data1[Target],
                                                                                        random_state=0
                                                                                        )
train1_X_dummy, test1_X_dummy, train1_Y_dummy, test1_Y_dummy = model_selection.train_test_split(data1[data1_x_dummy],
                                                                                                data1[Target],
                                                                                                random_state=0
                                                                                                )
print("Data1 Shape: {}".format(data1.shape))
print("Train1 Shape: {}".format(train1_X.shape))
print("Test1 Shape: {}".format(test1_X.shape))

for x in data1_x:
    if data1[x].dtype != "float64":
        print("Survival Correlation by:", x)
        print(data1[[x, Target[0]]].groupby(x, as_index=False).mean())
        print("-"*25)
        
print(pd.crosstab(data1["Title"], data1[Target[0]]))

plt.figure(figsize=[16,12])

plt.subplot(231)
plt.boxplot(x=data1["Fare"], showmeans=True, meanline=True)
plt.title("Fare Boxplot")
plt.ylabel("Fare $")

plt.subplot(232)
plt.boxplot(data1["Age"], showmeans=True, meanline=True)
plt.title("Age Boxplot")
plt.ylabel("Age (Years)")

plt.subplot(233)
plt.boxplot(data1["FamilySize"], showmeans=True, meanline=True)
plt.title("Family Size Boxplot")
plt.ylabel("Famile Size (#)")
        
plt.subplot(234)
plt.hist(x = [data1[data1["Survived"]==1]["Fare"], data1[data1["Survived"]==0]["Fare"]],
         stacked=True, color=["g", "r"], label=["Survived", "Dead"])
plt.title("Fare Histogram by Survival")
plt.xlabel("Fare ($)")
plt.ylabel("# Passengers")
plt.legend()

plt.subplot(235)
plt.hist(x=[data1[data1["Survived"]==1]["Age"], data1[data1["Survived"]==0]["Age"]],
         stacked=True, color=["g", "r"], label=["Survived", "Dead"])
plt.title("Age Histogram by Survival")
plt.xlabel("Age (Years)")
plt.ylabel("# Passengers")
plt.legend()

plt.subplot(236)
plt.hist(x=[data1[data1["Survived"]==1]["FamilySize"], data1[data1["Survived"]==0]["FamilySize"]],
         stacked=True, color=["g", "r"], label=["Survived", "Dead"])
plt.title("Family Size Histogram by Survival")
plt.xlabel("Family Size by #")
plt.ylabel("# of Passengers")
plt.legend()

plt.show()