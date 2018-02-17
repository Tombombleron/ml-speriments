# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:37:50 2018

@author: Robert
"""

import pandas as pd
import matplotlib.pyplot as plt

pokemon = pd.read_csv("../Data/pokemon.csv")

def ex_one():
    ax, axarr = plt.subplots(2, 1, figsize=(8, 8))
    
def ex_two():
    ax, axarr = plt.subplots(2, 1, figsize=(8, 8))
    pokemon["Attack"].plot.hist(
            ax=axarr[0],
            title="Pokemon Attack Ratings"
            )
    pokemon["Defense"].plot.hist(
            ax=axarr[1],
            title="Pokemon Defense Rating"
            )    
    
ex_two()