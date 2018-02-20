# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:53:31 2018

@author: Robert
"""

from __future__ import division
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("C:\Users\Robert\Google Drive\Online Learning\Stanford - Machine Learning\Week 2\Programming Assignment\machine-learning-ex1\ex1\ex1data2.txt", header=None, names=["size_ft", "num_b-rooms", "price"])

data1 = data.copy()
y = data1.price
x_cols = ["size_ft", "num_b-rooms"]
X = data1[x_cols]

def featureNormalize(X):
    combo_X = np.array(X)
    
    X_sigma = [X.size_ft.std(), X["num_b-rooms"].std()]
    
    X_mu = [X.size_ft.mean(), X["num_b-rooms"].mean()]
    
    for i in range(0, len(combo_X)):
        for j in range(0, len(combo_X[i])):
            combo_X[i][j]-=X_mu[i]
            combo_X[i][j]/=X_sigma[i]
    
    result_X = pd.DataFrame(data=combo_X)
    print result_X
    return result_X
    
featureNormalize(X)