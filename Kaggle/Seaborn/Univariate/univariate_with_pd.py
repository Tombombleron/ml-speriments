#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:13:39 2018

@author: tombombleron
"""

import pandas as pd

reviews = pd.read_csv("winemag-data_first150k.csv", index_col=0)

#reviews["province"].value_counts().head(10).plot.bar()
#(reviews["province"].value_counts().head(10) / len(reviews)).plot.bar()
#reviews["points"].value_counts().sort_index().plot.bar()
#reviews["points"].value_counts().sort_index().plot.line()
#reviews[reviews["price"] < 100]["price"].plot.hist()
reviews["points"].plot.hist()
