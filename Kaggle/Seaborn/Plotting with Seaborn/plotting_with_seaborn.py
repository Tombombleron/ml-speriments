#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:28:33 2018

@author: tombombleron
"""

import pandas as pd
import seaborn as sns

reviews = pd.read_csv("winemag-data_first150k.csv")

df = reviews[reviews.variety.isin(reviews.variety.value_counts().head(5).index)]

#sns.countplot(reviews["points"])
#sns.kdeplot(reviews.query("price < 200").price)
#sns.kdeplot(reviews[reviews['price'] < 200].loc[:, ['price', 'points']].dropna().sample(5000))
#sns.distplot(reviews["points"],bins=10,kde=False)
#sns.jointplot(x="price", y="points", data=reviews[reviews["price"] < 100],kind="hex",gridsize=20)
#sns.boxplot(
#        x="variety",
#        y="points",
#        data=df
#        )
#sns.violinplot(
#        x="variety",
#        y="points",
#        data=reviews[reviews.variety.isin(reviews.variety.value_counts()[:5].index)]
#        )

pokemon = pd.read_csv("Pokemon.csv", index_col=0)
dataf = pokemon[pokemon.Legendary.isin(pokemon.Legendary.value_counts().head(5).index)]
#sns.countplot(pokemon["Generation"])
#sns.distplot(pokemon["HP"], bins=40, kde=True)
#sns.jointplot(x="Attack",
#              y="Defense",
#              data=pokemon)
#sns.jointplot(x="Attack",
#              y="Defense",
#              data=pokemon,
#              kind="hex",
#              gridsize=20
#              )
#fig = sns.kdeplot(pokemon["HP"], pokemon["Attack"], shade=True, )
#fig.figure.suptitle("Pokemon HP plotted against Pokemon Attack")

#sns.boxplot(
#        x="Legendary",
#        y="Attack",
#        data=dataf
#        )
sns.violinplot(
        x="Legendary",
        y="Attack",
        data=dataf
        )