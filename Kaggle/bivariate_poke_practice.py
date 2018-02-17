#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:31:59 2018

@author: tombombleron
"""

import pandas as pd

pd.set_option("max_columns", None)
data = pd.read_csv("pokemon.csv")

pokemon_stats_legendary = data.groupby(['is_legendary', 'generation']).mean()[['attack', 'defense']]
pokemon_stats_by_generation = data.groupby('generation').mean()[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
#data.columns = [cols.replace(" ", "_").lower() for cols in data.columns]

#data.plot.scatter(x="attack", y="defense")
#data.plot.hexbin(x="attack", y="defense", gridsize=20)

#pokemon_stats_legendary.plot.bar(stacked=True)

pokemon_stats_by_generation.plot.line()