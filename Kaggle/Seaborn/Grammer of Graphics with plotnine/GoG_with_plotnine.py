# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 09:05:32 2018

@author: Robert
"""

import pandas as pd
import plotnine as pn

reviews = pd.read_csv("../Data/winemag-data-130k-v2.csv", index_col=0)

top_wines = reviews[reviews["variety"].isin(reviews["variety"].value_counts().head(5).index)]

def simple_scatter():
    df = top_wines.head(1000).dropna()
    
    (pn.ggplot(df)
    + pn.aes("points", "price")
    + pn.geom_point()
    )
    
simple_scatter()