# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 16:15:01 2020

@author: HeSer
# """

import pandas as pd

df = pd.read_csv("Data/albumlist.csv")

# print(df)
# import seaborn as sns

# for row in df:
#     print(row)
    
# rows = 101
# for row in df: 
#     rows -= 1 
#     if (rows > 0):
#         print(row)
#     else:
#         break
    
for row in df:
    print(row)