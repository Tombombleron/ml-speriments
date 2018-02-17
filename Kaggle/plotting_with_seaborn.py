#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:28:33 2018

@author: tombombleron
"""

import pandas as pd
import seaborn as sns

reviews = pd.read_csv("../Wine/winemag-data_first150k.csv")

#sns.countplot(reviews["points"])
#sns.kdeplot(reviews.query("price < 200").price)
#sns.kdeplot(reviews[reviews['price'] < 200].loc[:, ['price', 'points']].dropna().sample(5000))
#sns.distplot(reviews["points"],bins=10,kde=False)
sns.jointplot(x="price", y="points", data=reviews[reviews["price"] < 100],kind="hex",gridsize=20)