# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:58:52 2020

@author: HeSer
"""

import pandas as pd 

# fi = open("../Wharton_M3.py", "w")
# fi

# # for lin in fi:
# #     print(lin)

# fi.close()

# file_object = open("square.txt", "w")
# for number in range(13):
#     square = number * number
#     print(square)

# file_object.write(
#                     # for me in range(50):
#                     #     x = []
#                     #     if me % 2 == 0:
#                     #         x = x.append(me**2)
#                     #     else:
#                     #         continue
                   
#     "##This is to check if what I do is what I think I do!"'\n'
#     "## So far I am partially there. "'\n'
#     "## so the question is how to add functions and formulas to the text, when I want to write a file. ")


# file_object

# file_object.close()

## So, I read a file
# new_file_object = open("square.txt", "r")
# print(new_file_object.read()[:150])

with open ("square.txt", "r") as md:
    for line in md:
        print(line)
        
# Start from CSV lectures. 