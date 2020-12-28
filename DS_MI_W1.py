# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 23:18:58 2020

@author: HeSer
"""
import csv


with open ("mpg.csv") as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
mpg[:3]
