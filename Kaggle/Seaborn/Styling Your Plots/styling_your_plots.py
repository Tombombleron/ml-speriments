# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:00:59 2018

@author: Robert
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

reviews = pd.read_csv("../Data/winemag-data_first150k.csv")

#reviews["points"].value_counts().sort_index().plot.bar(
#        figsize=(12,6),
#        color="lightblue",
#        fontsize=16,
#        title="Rankings Given By Wine Magazine"
#        )

ax = reviews["points"].value_counts().sort_index().plot.bar(
        figsize=(12,6),
        color="lightblue",
        fontsize=16
        )

ax.set_title("Rankings Given by Wine Magazine", fontsize=20)
sns.despine(bottom=True, left=True)