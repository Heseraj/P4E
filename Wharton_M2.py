# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:17:21 2020

@author: HeSer
"""

# your_score = int(input("Enter you Score "))
# if your_score > 100 or your_score < 0:
#     print("sorry! This can't be your socre, try again")
#     your_score = int(input("Enter your correct Score "))
#     if your_score > 100 or your_score < 0:
#         print("again, sorry, this can't be your number -:(")
#         your_score = int(input("Please, Please enter your correct Score on last time!"))
#         if your_score >= 90:
#             print("Finally, A")
#         elif your_score >= 80:
#             print("B")
#         elif your_score >= 70:
#             print("C")
#         elif your_score >= 60:
#             print("D")
#         elif your_score > 100 or your_score < 0:
#             print("You need to go to the registrat Office to sort your issue out")
#         else:
#             print("Unfortunately, You need to repeat the class !")
#     elif your_score >= 90:
#         print("Congratulation you got A for the class")
#     elif your_score >= 80:
#         print("your got B for the class")
#     elif your_score >= 70:
#         print("You got C for the class")
#     elif your_score >= 60:
#         print("you got D for the class")
#     else:
#         print("You need to repeat the class")
# elif your_score >= 90:
#     print("Congratulation you got A for the class")
# elif your_score >= 80:
#     print("your got B for the class")
# elif your_score >= 70:
#     print("You got C for the class")
# elif your_score >= 60:
#     print("you got D for the class")
# else:
#     print("you need to repeat the class")

# now, coding seems fun as I can find my way aruond. ''


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in numbers:
#     print(x)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in numbers:
#     if(x == 10):
#         print(x)
#     elif x <= 10:
#         print(10 - x)
#     else:
#         print("Operation compo")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# even_numbers = []
# odd_numbers = []
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
#     else:
#         odd_numbers.append(number)
# print(even_numbers,"mext list" ,odd_numbers)

# even_numbers = []
# odd_numbers = []
# Iteration_count = 0
# even_count = 0
# odd_count = 0
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
#         even_count += 1
#     else:
#         odd_numbers.append(number)
#         odd_count += 1
# print(even_numbers, "and the count is ",even_count)
# print(odd_numbers,"and the count is " ,odd_count)

# ## Planet example
# planets = ["sun", "mercury", "venus", "earth", "mars", "nepton"]
# for planet in planets:
#     # if (planet != planets):
#     #     print("sorry, this is not in the planets list")
#     if (planet == "sun"):
#     # elif (planet == "sun"):
#         print("sorry!", planet, "is not a planet. It is a star")
#     elif (planet == "mercury"):
#         print(planet, "is the closes to the Sun")
#     else:
#         print(planet, "is a planet!")


# month = "February"
# for letter in month:
#     print(letter)


# rg_num= range(1, 100,3)
# for x in rg_num:
#     print(x)


# num_list = 1000
# e_list = []
# o_list = []
# re_num = []
# for num in range(0,num_list, 5):
#     if(num % 10 == 0):
#         e_list.append(num)
#     elif (num % 3 == 0):
#         o_list.append(num)
#     else:
#         re_num.append(num)
# print(e_list)
# print(o_list)
# print(re_num)
# print("Check if you have all the numbers by suming up the length",len(e_list) + len(o_list) + len(re_num))

# even_numbers = []

# for num in range(1, 21):
#     if(num % 2 == 0):
#         even_numbers.append(num)
# print(even_numbers)

#

# name = input("What is your name? ")
# let_count = 0
# for let in name:
#     print(let)
#     let_count += 1
# print("count is",let_count)

# x = 5
# while(x > 0):
#     print(x)
#     x -= 1


# counter = 0
# x = 2
# while(x < 10000):
#     print("is is now:", x)
#     counter += 1
#     x = x *2
#     print("x has become now: ", x )
# print("the count of operation is", counter)


# ##While loop example
# counter = 1
# maximum_try = 10
# answer = input("What is the biggest selling album of all time? ")
# while(answer != "Thriller"):
#     print("Sorry! The naswer is not correct, try again")
#     counter += 1
#     answer = input("What is the ablum? ")
#     print("your try is ", counter)
# print("finaly you got the naswer after", counter, "guessings.", "The answer is", answer)


##While loop example
# counter = 1
# maximum_try = 5
# answer = input("What is the biggest selling album of all time? ")
# while(answer != "Thriller"):
#     print("Sorry! The naswer is not correct, try again")
#     counter += 1
#     answer = input("What is the ablum? ")
#     print("your try is ", counter)
#     if (counter == maximum_try and answer != "Thriller"):
#         print("sorry, you lost all your tries")
#         break
#     elif(counter == maximum_try - 1 and answer != "Thriller"):
#         print("Warning, Wharning, You only got one last chance left!")
#     elif(answer == "Thriller" and counter == maximum_try):
#         print("finaly you got the naswer after", counter, "guessings.", "The answer is", answer)

# # breaking while loop
# x = 1
# while x <= 10:
#     if (x == 5):
#         break
#     print("x is now", x)
#     x += 1

# # the continue function
# x = 1
# for x in range(1,30):
#     if x == 5:
#         continue
#     print("x is now", x)
#     x += 1

# Nested loops
for i in range(1, 11):
    for j in range(1, 11):
        print("{0} * {1} : {2}".fomrat(i, j, i * j))

# #working with lists
# list_1 = ["dog", "cat", 789, "book", ["extract me please",11, 20, "sea"]]
# # print(list_1[1])

# # print(list_1[4][0][9])
# # # print(list_1[2])
# # print(list_1[4][0])

# print(list_1.index("cat"))

#slicing a list
# my_list = [1, 2, 3, 4, 5, ["hello", "How", "was", 11, "th", "day"], 6, 9, 11, 10, 18]
# # print(my_list[4:7])
# # print(my_list[4:6])
# # print(my_list[3:])
# # print(my_list[:6])
# print(my_list[:-5])

# # replayce least of elements
# odd_list = [2, 4, 6, 8, 10]

# # for num in range(odd_list):
# # 	if num / 2 == 0:
# # 		num += 1
# # 		odd_list[num] = odd_list[num]
# # print(odd_list)

# odd_list[:4] = [1, 3, 5, 7]
# print(odd_list)

# Practice

# name = input("What is your name? ")
# print(name[0:4])

#More practice
# name = input("What is your name? ")
# # f_name = input( "of the", name, "what is your first name ")
# in_name = name.index(" ")
# print(name[:in_name])


#Dictionary
my_dictionary = {"age": 40, "name": "Mosa", "height": 6*12+3}
print(my_dictionary)

print(type(my_dictionary))

#Some practices for the Dict portion is left that I didn't do. I also need to check the homework for module 2
