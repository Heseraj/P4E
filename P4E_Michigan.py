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

num_list = 100
e_list = []
o_list = []
re_num = []
for num in range(num_list):
    if(num % 5 == 0):
        e_list.append(num)
    elif (num % 3 == 0):
        o_list.append(num)
    else:
        re_num.append(num)
print(e_list)
print(o_list)
print(re_num)
print("Check if you have all the numbers by suming up the length",len(e_list) + len(o_list) + len(re_num))
