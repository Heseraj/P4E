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


even_numbers = []
odd_numbers = []
Iteration_count = 0
even_count = 0
odd_count = 0
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        even_count += 1
    else:
        odd_numbers.append(number)
        odd_count += 1
print(even_numbers, "and the count is ",even_count)
print(odd_numbers,"and the count is " ,odd_count)