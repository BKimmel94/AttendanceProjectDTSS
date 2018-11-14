# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

att_breakdown = pd.read_csv('/Users/billykimmel/Mathnasium_Attendance/Fall_2018.csv')

att_data = pd.read_csv('/Users/billykimmel/Mathnasium_Attendance/Fall_18_Useful.csv')

att_data['Date'] = pd.to_datetime(att_data['Date'], infer_datetime_format = True)
print(att_data)

print(att_data[att_data.Atten_Total != 0].groupby('Day')['Percent'].mean())