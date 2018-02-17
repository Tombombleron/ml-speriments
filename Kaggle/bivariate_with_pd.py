#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:42:30 2018

@author: tombombleron
"""

import pandas as pd

reviews = pd.read_csv("winemag-data_first150k.csv", index_col=0)

#reviews[reviews["price"] < 100].sample(100).plot.scatter(x="price", y="points")
#reviews[reviews["price"] < 100].plot.hexbin(x="price", y="points", gridsize=15)

wine_counts = pd.read_csv("top-five-wine-score-counts.csv", index_col=0)
wine_counts.columns = [col.replace(" ", "_").lower() for col in wine_counts.columns]

#wine_counts.plot.bar(stacked=True)
#wine_counts.plot.area()
wine_counts.plot.line()
