# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:46:35 2020

@author: HeSer
"""

import csv 
with open("Data/albumlist.csv", "r") as df:
    reader = csv.DictReader(df)

# print(type(reader))
# print(reader.fieldnames)

for row in reader: 
    print(row)