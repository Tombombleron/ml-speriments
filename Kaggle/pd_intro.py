#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:07:02 2018

@author: tombombleron
"""

import pandas as pd

data = pd.read_csv("parks.csv")

data.columns = [col.replace(" ", "_").lower() for col in data.columns]