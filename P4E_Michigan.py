# print("Hello World!, this is the new start")
#

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# even_numbers = []
# odd_numbers = []
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
#     else:
#         odd_numbers.append(number)
# print(even_numbers,"mext list" ,odd_numbers)
#
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
# print(even_numbers, "and the count is ", even_count)
# print(odd_numbers, "and the count is ", odd_count)
#
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
#
# month = "February"
# for letter in month:
#     print(letter)
#
# num_list = 100
# e_list = []
# o_list = []
# re_num = []
# for num in range(num_list):
#     if(num % 5 == 0):
#         e_list.append(num)
#     elif (num % 3 == 0):
#         o_list.append(num)
#     else:
#         re_num.append(num)
# print(e_list)
# print(o_list)
# print(re_num)
# print("Check if you have all the numbers by suming up the length",len(e_list) + len(o_list) + len(re_num))
# expanded list of playing with numbers
num_list = 1000
e_list = []
o_list = []
re_num = []
for num in range(0,num_list, 5):
    if(num % 10 == 0):
        e_list.append(num)
    elif (num % 3 == 0):
        o_list.append(num)
    else:
        re_num.append(num)
print(e_list)
print(o_list)
print(re_num)
print("Check if you have all the numbers by suming up the length",len(e_list) + len(o_list) + len(re_num))

# breaking while loop
x = 1
while x <= 10:
    if (x == 5):
        break
    print("x is now", x)
    x += 1

# the continue function
for x in range(1, 10):
    if x == 5:
        continue
    print("x is now", x)
    x += 1

# Nested loops
for i in range(1, 11):
    for j in range(1, 11):
        print("{} *{} = {}".fomrat(i, j, i * j))
##I don't know what it doesn't work This is a good question to ask from Sajjad

#working with lists
list_1 = ["dog", "cat", 789, "book", ["extract me please", 11, 20, "sea"]]
print(list_1[1])

print(list_1[4[0]])
print(list_1[2])
#slicing a list, remember you should always use the function print on spyder, ohterwise, your code doens't work
my_list = [1, 2, 3, 4, 5, ["hello", "How", "was", 11, "th", "day"], 6, 9]
print(my_list[4:7])

# replayce least of elements
odd_list = [2, 4, 6, 8, 10]

for num in odd_list:
	if num / 2 == 0:
		num += 1
		odd_list = odd_list.append(num)
print(odd_list)


#practice

name = input("What is your name? ")
f_name = input("of the ", name, "which one is your first name?")
print(name[0, len(f_name)])

#Dictionary
my_dictionary = {"age": 40, "name": "Mosa", "height": 6*12+3}
print(my_dictionary)
