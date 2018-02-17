# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:42:37 2018

@author: Robert
"""

import pandas as pd
import re
import numpy as np
import seaborn as sns

pd.set_option("max_columns", None)
df = pd.read_csv("../Fifa/CompleteDataset.csv", index_col=0)
footballers = df.copy()
footballers = footballers.assign(Position=footballers['Preferred Positions'].str.split().str[0])


def lmplot_plot():
    sns.lmplot(x="Overall", y="Special", hue="Position",
               data=footballers.loc[footballers["Position"].isin(["ST", "RW", "LW"])],
               fit_reg=False)
    
def lmplot_shapes_plot():
    sns.lmplot(x="Overall", y="Special", markers=["o", "x", "*"], hue="Position",
               data=footballers.loc[footballers["Position"].isin(["ST", "RW", "LW"])],
               fit_reg=False)
    
def box_plots():
    f = (footballers
         .loc[footballers["Position"].isin(["ST", "GK"])]
         .loc[:, ["Overall", "Aggression", "Position"]]
         )
    f = f[f["Overall"] >= 80]
    f = f[f["Overall"] < 85]
    f["Aggression"] = f["Aggression"].astype(float)
    
    sns.boxplot(x="Overall", y="Aggression", hue="Position", data=f)
    
def heatmapz():
    f = (
            footballers.loc[:,["Acceleration", "Aggression", "Agility", "Balance", "Ball Control"]]
            .applymap(lambda v: int(v) if str.isd else np.nan)
            .dropna()
            ).corr()
    
    sns.heatmap(f, annot=True)
    
heatmapz()