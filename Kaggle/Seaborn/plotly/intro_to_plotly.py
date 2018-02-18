# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 08:33:18 2018

@author: Robert
"""

import pandas as pd
from plotly.offline import init_notebook_mode, plot
import plotly.graph_objs as go
init_notebook_mode(connected=True)

reviews= pd.read_csv("../Data/winemag-data-130k-v2.csv")

def scatter_plot():
    plot([go.Scatter(x=reviews.head(1000)["points"], y=reviews.head(1000)["price"], mode="markers")])
    
def KDE_plot():
    plot([go.Histogram2dContour(x=reviews.head(500)["points"],
                                 y=reviews.head(500)["price"],
                                 contours=go.Contours(coloring="heatmap")),
                                 go.Scatter(x=reviews.head(1000)["points"], y=reviews.head(1000)["price"], mode="markers")
                                 ])
    
def surface_plot():
    df = reviews.assign(n=0).groupby(["points", "price"])["n"].count().reset_index()
    df = df[df["price"] < 100]
    v = df.pivot(index="price", columns="points", values="n").fillna(0).values.tolist()
    plot([go.Surface(z=v)])
    
def choropleth_plot():
    df = reviews["country"].replace("US", "United States").value_counts()
    
    plot([go.Choropleth(
            locationmode="country names",
            locations=df.index.values,
            text=df.index,
            z=df.values
            )])