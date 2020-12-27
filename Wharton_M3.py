# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:56:36 2020

@author: HeSer
"""

# def square(x):
# 	y = x * x
# 	return y

# to_square = int(input("Eneter the Number _:) "))
# result = square(to_square)
# print(result)


def greater_than (x, y):
 	if x > y:
          return True
 	else:
          return False

# a = 2
# b = 5

# result = greater_than(a, b)
# print("{} is greater than {}: {}".format(a, b, result))

#This is from Module two, figuring out nested loops

# # Nested loops
# for i in range(1, 11):
#     for j in range(1, 11):
#         print("{} * {} : {}".fomrat(i, j, i * j))
##Still I can't figure this out


# def absolute_value(x):
# 	if x >= 0:
# 		return x
# 	else:
# 		return -1 * x

# c = -10
# d = 2.5
# result = absolute_value(d)
# print(result)

# num_list = int(-10, 5, 0.5, -0.5, 12, 5, 7)

# # for i in num_list:
# #     result = greater_than[num_list[i]]
# #     return result

# for i in len(num_list):
#     num_list = num_list[i]
#     print(num_list)

# z = 10
# q = 15
# result = greater_than(z, q)
# print("The result is",result)


# def f_to_c(t):
# 	return (t - 32) * 5.0 / 9.0

# def print_c_from_f():
# 	f = int(input("What is the temprature today? "))
# 	c = f_to_c(f)
# 	print(c)

# print_c_from_f()


# def greet():
# 	name = input("what is your name? ")
# 	print("Hello", name, "Good Morning!")

# greet()

#  num_list = [1 ,2 ,3 ,3 ,4 ,4 , 6, 6, 7]

#  def Uniquie_list(num_list):
# 	 x = []
# 	 for i in num_list:
# 		 if i not in num_list:
# 			 x.append(i)
# 	 return x

# class Customer(object):
# 	"""A customr is client of ABC bank,
# 	Customers can provide a 'name' and their balance"""
# 	#Initializer
# 	def __init__(self, name, balance = 0.0):
# 		self.name = name
# 		self.balance = balance
# 	def deposit(self, amount):
# 		self.balance += amount
# 		return self.balance
# 	def withdraw(self, amount):
# 		if (amount > self.balance):
# 			raise RuntimeError("You don't have enough balance")
# 		self.balance -= amount
# 		return self.balance
# 	def purchase(self, amount):
# 		purchase = sum(amount)
# 		if purchase > self.balance:
# 			raise RuntimeError("Not enough Balance")
# 		else:
# 			self.balance -= purchase
# 			print("your purchase amount is", purchase)
# 			print("your remaining balance is", self.balance)
# 			return self.balance


# customer1 = Customer("Mosa Rahimi", balance = 1200)

# print(customer1)

import random

restaurants = ["Vetri", "Barbuzzo", "Vedge", "Laurel", "McDonalds", "Burger King", "Wndyees"]
def pick_restaurant():
 	rand_int = random.randint(0, len(restaurants) - 1 )
 	return restaurants[rand_int]

restaurants.append("KFC")
print(restaurants)

print(pick_restaurant())
print(pick_restaurant())