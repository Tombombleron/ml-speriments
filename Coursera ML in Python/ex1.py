# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:55:16 2018

@author: Robert
"""

from __future__ import division
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from time import sleep

data = pd.read_csv("C:\Users\Robert\Google Drive\Online Learning\Stanford - Machine Learning\Week 2\Programming Assignment\machine-learning-ex1\ex1\ex1data1.txt", header=None, names=["x", "y"])

data1 = data.copy()
data1 = data1.assign(x_0 = lambda z: z.x/z.x)
X = data1.x
y = data1.y
theta = [0, 0]


def plotData(data, X, y):
    sns.regplot(x=X, y=y, data=data, fit_reg=False, marker="x")
    plt.ylabel("Revenue in $10ks")
    plt.xlabel("Customers in 10ks")
    plt.show()
    
def computeHTheta(theta, X):
    result = []
    for i in range(0, len(X)):
        result.append(theta[0] + (theta[1] * X[i]))
        
    return result
    
def computeCost(X, y, theta):
    sqrErrors = []
    m = len(y)
    for i in range(0, m):
        sqrError = ((theta[0] + (theta[1] * X[i])) - y[i])**2
        sqrErrors.append(sqrError)
        
    cost = (1 / (2 * m)) * sum(sqrErrors)
        
    print "-"*25
    print "cost:", cost
    return cost

def gradientDescent(data, iterations=1500, alpha=0.01, theta=[0, 0]):
    X = data.x
    m = len(data.y)
    jHistory = []
    
    for iter in range(1, iterations):
        error0 = []
        error1 = []
        for i in range(0, m):
            error0.append(((theta[0] + (theta[1] * X[i])) - y[i]))
            error1.append(((theta[0] + (theta[1] * X[i])) - y[i])*X[i])
        theta[0] = theta[0] - alpha / m * sum(error0)
        theta[1] = theta[1] - alpha / m * sum(error1)
        
        jTheta = computeCost(data.x, data.y, theta)
        jHistory.append(jTheta)

    plt.close()
    sns.kdeplot(jHistory, legend=False)
    plt.ylabel("Cost J(theta)")
    plt.xlabel("Number of iterations")
    plt.show()
        
    print "-"*25
    print "theta minimise J(theta):", theta
    return theta

plotData(data1, X, y)
sleep(5)
computeCost(X, y, theta)
sleep(5)
gradientDescent(data1)