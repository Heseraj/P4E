# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:43:36 2020

@author: HeSer
"""

# import pandas as pd 
# # xlx = pd.read_excel("Data/imdb.xlsx")


# xls = pd.ExcelFile("Data/yelp.xlsx")
# df2 = xls.parse("yelp_data")

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

# # for multiple columns 
# # print(df2[["name", "category_0", "city_id", "state_id"]])

# ###The way I see it there is a difference between what one says to the console and on the text writer

# ###The way I see this, Python is much eaiser and much intuitive for workings 

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

# import random

# stars = divebars_Iv["stars"] >= 4.0
# diverbars_4rating_Iv = divebars_Iv[stars]
# rand_int = random.randint(0, len(diverbars_4rating_Iv) - 1)
# rand_divebar = diverbars_4rating_Iv[rand_int:rand_int + 1]
# print("Here's one with a", rand_divebar["stars"].iloc[0], "rating.")
# print(rand_divebar[["name", "stars", "review_count"]])


# df["categories"] = df["category_0"].str.cat(df["category_1"], sep = " , ")

# ## add a new columns that takes stars into a rating out of ten
# df["ratings"] = df["stars"] *2
# print(df.head(100))
# df[["stars", "ratings"]]

# ## rating out of 20 

# def convert_to_ratings(x): 
#     return(str(x) + " The space is intentional out of 20")

# # df["rating_20"] = df["ratings"] *2 
# # df["rating_20"]

# df["ratings_20"] = df["rating_20"].apply(convert_to_ratings)

# print(df.head(20))


# ### Group Data 

# # df.groupby(["city"]).group.keys() ## Why I get it wrong 

#print(len(df.groupby(["city"]).groups["Las Vegas"]))

### the pivot table and numpy was left out of the course, It means I have to come and pracitce it later. 


# Working on visuliazations 

import matplotlib.pyplot as plt 
import numpy as np

# df_pitt = df[df["city"] == "Pittsburgh"]
# df_vegas = df[df["city"] == "Las Vegas"]


# series_vegas = df_vegas["stars"]
# series_pitt = df_pitt["stars"]
# series_pitt10 = df_pitt["ratings"]
# series_vegas_10 = df_vegas["ratings"]
# # plt.hist(series_pitt, 
# #          alpha = 0.3,
# #          color = "yellow",
# #          label = "Pittsburgh",
# #          bins = "auto")

# plt.hist(series_pitt10, 
#           alpha = 0.3,
#           color = "blue",
#           label = "Pittsburgh",
#           bins = "auto")

# # plt.hist(series_vegas, 
# #          alpha = 0.5,
# #          color= "red",
# #          label = "Las Vegas",
# #          bins = "auto"
# #          )
# # plt.xlabel("ratings")
# # plt.ylabel("number of rating scores")


# plt.hist(series_vegas_10, 
#          alpha = 0.5,
#          color= "red",
#          label = "Las Vegas",
#          bins = "auto"
#          )
# plt.xlabel("ratings")
# plt.ylabel("number of rating scores")
# plt.legend(loc = "best")
# plt.title("Review of Distribution  of Pitsburgg and Las Vegas")


# plt.hist([series_pitt10, series_vegas_10], alpha = 0.7, color = ["red", "blue"],
#          label = ["Pitssburgh", "Las Vegas"], bins = "auto")

# plt.xlabel("Ratings")
# plt.ylabel("Number of Ratings Scores")
# plt.legend(loc = "best")
# plt.title("Review Distribution of Pitssburgh and Las Vegas")
# plt.show()


### Looking at Scatter Plots 

df_health = df[df["category_0"]== "Health & Medical"]
df_fast = df[df["category_0"]== "Fast Food"]
df_brunch = df[df["category_0"]== "Breakfast & Brunch"]

plt.scatter(df_health["stars"], df_health["review_count"],
            marker= "o",
            color = "r",
            alpha = 0.7,
            s= 124,
            label = ["Health & Medical"]
            )
plt.scatter(df_fast["stars"], df_fast["review_count"], 
            marker="h",
            color = "blue",
            alpha = 0.7,
            s = 124,
            label = ["Fast Food"]
            )
plt.scatter(df_brunch["stars"], df_brunch["review_count"],
            marker = "^",
            color = "green",
            alpha = 0.7,
            s = 124,
            label = ["Breakfast & Brunch"]
            )

plt.xlabel("Rating")
plt.ylabel("Review Count")
plt.legend(loc = "upper left")
axes = plt.gca()
axes.set_yscale("log")
plt.show()