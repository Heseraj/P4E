# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:43:36 2020

@author: HeSer
"""

import pandas as pd 
# xlx = pd.read_excel("Data/imdb.xlsx")


xls = pd.ExcelFile("Data/yelp.xlsx")
df2 = xls.parse("yelp_data")

# # print(type(df2))
# print(len(df2))
# print(df2.shape)
# print(df2.count)
# print(df2.columns)
# print(df2.dtypes)
# print(df2.describe())
# print(df2.head())
# print(df2.head(100))

# print(df2["city_id"])

# for multiple columns 
# print(df2[["name", "category_0", "city_id", "state_id"]])

# The way I see it there is a difference between what one says to the console and on the text writer

# The way I see this, Python is much eaiser and much intuitive for workings 

# df_cities = xls.parse("cities")

# df = pd.merge(df2, df_cities, how="inner", left_on=("city_id"), right_on=("id"))
# df_states = xls.parse("states")

# print(df_states)
# df = pd.merge(df, df_states, how = "inner", left_on=("state_id"), right_on = ("id"))

# print(df)

# print(df.info())
# print(df[2:5])

# print(df[100:200])

# last_index = len(df) - 1 
# last_business = df[last_index:]
# last_business["name"]
# df[-1:]["name"]

# pitts = df["city"]=="Pittsburgh"
# rest = df["name"] == "The Dragon Chinese Cuisine"
# bus = df[rest]["take_out"]
# bus.iloc[0]

# cat_0_bars = df["category_0"] == "Bars"
# cat_1_bars = df["category_1"] == "Bars"
# df[cat_0_bars |cat_1_bars]

# carnegie = df["city"] == "Carnegie"
# df[(cat_0_bars|cat_1_bars) & carnegie]

# carnegie_df = df[(cat_0_bars|cat_1_bars) & carnegie]

# cat_0 = df["category_0"].str.contains("Nail Salon")

# cat_1 = df["category_1"].str.contains("Nail Salon")
# henderson = df["city"] == "Henderson"
# df[(cat_0|cat_1) & henderson]["review_count"].sum()
# df["city"].unique()
# df["city"].value_counts()
# df["category_1"].nunique()


# Iv = df["city"] == "Las Vegas"
# cat_0_dive = df["category_0"] == "Dive Bars"
# cat_1_dive = df["category_1"] == "Dive Bars"
# divebars_Iv = df[Iv &(cat_0_dive | cat_1_dive)]
# print("there are ", len(divebars_Iv), "Dive bars in Las Vegas")

import random

stars = divebars_Iv["stars"] >= 4.0
diverbars_4rating_Iv = divebars_Iv[stars]
rand_int = random.randint(0, len(diverbars_4rating_Iv) - 1)
rand_divebar = diverbars_4rating_Iv[rand_int:rand_int + 1]
print("Here's one with a", rand_divebar["stars"].iloc[0], "rating.")
print(rand_divebar[["name", "stars", "review_count"]])


