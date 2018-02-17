# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:31:23 2018

@author: Robert
"""

import pandas as pd
import seaborn as sns

pokemon = pd.read_csv("../Pokemon.csv")


poke_copy = pokemon.copy()

#g = sns.FacetGrid(poke_copy, row="Legendary")
#g.map(sns.kdeplot, "Attack")
#
#g = sns.FacetGrid(poke_copy, col="Legendary", row="Generation")
#g.map(sns.kdeplot, "Attack")

sns.pairplot(poke_copy[["HP", "Attack", "Defense"]])