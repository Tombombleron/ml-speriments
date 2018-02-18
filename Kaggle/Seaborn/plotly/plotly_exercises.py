# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 09:01:22 2018

@author: Robert
"""

import pandas as pd
from plotly.offline import init_notebook_mode, plot
import plotly.graph_objs as go
init_notebook_mode(connected=True)

pokemon = pd.read_csv("../Data/pokemon.csv")

def scatter_plot():
    plot([go.Scatter(x=pokemon["Attack"],
                     y=pokemon["Defense"],
                     mode="markers"
                     )])