#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:31:59 2018

@author: tombombleron
"""

import pandas as pd

pd.set_option("max_columns", None)
data = pd.read_csv("pokemon.csv")

data.columns = [cols.replace(" ", "_").lower() for cols in data.columns]

#data["type1"].value_counts().plot.bar()
#data["hp"].value_counts().sort_index().plot.line()
data["weight_kg"].plot.hist()