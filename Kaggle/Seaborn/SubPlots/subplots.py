# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:29:10 2018

@author: Robert
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

reviews = pd.read_csv("../Data/winemag-data_first150k.csv")

def subplot_two_one():
    # plots 2 rows and 1 column.
    fig, axarr = plt.subplots(2, 1, figsize=(12,8))
    
    reviews["points"].value_counts().sort_index().plot.bar(
            ax=axarr[0],
            color="grey"
            )
    
    reviews["province"].value_counts().head(20).plot.bar(
            ax=axarr[1],
            color="lightblue"
            )
    
def subplot_two_two():
    fig, axarr = plt.subplots(2, 2, figsize=(12,8))
    
    reviews["points"].value_counts().sort_index().plot.bar(
            ax=axarr[0][0],
            color="grey"
            )
    
    reviews["province"].value_counts().head(20).plot.bar(
            ax=axarr[1][1],
            color="lightblue"
            )
    
def bear_graphic():
    fig, axarr = plt.subplots(2, 2, figsize=(12, 8))

    reviews['points'].value_counts().sort_index().plot.bar(
        ax=axarr[0][0], fontsize=12, color='mediumvioletred'
    )
    axarr[0][0].set_title("Wine Scores", fontsize=18)
    
    reviews['variety'].value_counts().head(20).plot.bar(
        ax=axarr[1][0], fontsize=12, color='mediumvioletred'
    )
    axarr[1][0].set_title("Wine Varieties", fontsize=18)
    
    reviews['province'].value_counts().head(20).plot.bar(
        ax=axarr[1][1], fontsize=12, color='mediumvioletred'
    )
    axarr[1][1].set_title("Wine Origins", fontsize=18)
    
    reviews['price'].value_counts().plot.hist(
        ax=axarr[0][1], fontsize=12, color='mediumvioletred'
    )
    axarr[0][1].set_title("Wine Prices", fontsize=18)
    
    plt.subplots_adjust(hspace=.3)
    
    sns.despine()