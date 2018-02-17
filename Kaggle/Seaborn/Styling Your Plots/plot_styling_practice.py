# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:20:51 2018

@author: Robert
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def scatter_plot():
    pokemon.plot.scatter(x="Attack",
                         y="Defense",
                         figsize=(12, 6),
                         title="Pokemon by Attack and Defense"
                         )

def hist_plot():
    pokemon["Total"].plot.hist(
            bins=40,
            color="grey",
            title="Pokemon by Stat Total",
            figsize=(12,6)
            )

def bar_chart():
    pokemon["Type 1"].value_counts().plot.bar(
            figsize=(12,6),
            title="Pokemon by Primary Type",
            color="lightblue"
            )

pokemon = pd.read_csv("../Data/pokemon.csv")
