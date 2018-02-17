# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:05:25 2018

@author: Robert
"""

import pandas as pd
import seaborn as sns
pd.set_option('max_columns', None)
df = pd.read_csv("CompleteDataset.csv", index_col=0)
pos_data = pd.read_csv("PlayerPlayingPositionData.csv", index_col=0)

import re
import numpy as np

footballers = df.copy()
footballers = footballers.assign(Position=footballers["Preferred Positions"].str.split().str[0])

#df1 = footballers[footballers["Positioning"].isin(["90", "92"])]
#g = sns.FacetGrid(df1, col="Positioning")
#g.map(sns.kdeplot, "Overall")

#df1 = footballers
#g = sns.FacetGrid(df1, col="Positioning", col_wrap=6)
#g.map(sns.kdeplot, "Overall")
#
#df1 = footballers[footballers["Position"].isin(["GK", "ST"])]
#df1 = df1[df1['Club'].isin(['Real Madrid CF', 'FC Barcelona', 'Atlético Madrid'])]
#g = sns.FacetGrid(df1, row="Position", col="Club")
#g.map(sns.violinplot, "Overall")

sns.pairplot(footballers[["Overall", "Potential", "Positioning"]])