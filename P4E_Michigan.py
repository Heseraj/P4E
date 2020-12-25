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
print(even_numbers, "and the count is ", even_count)
print(odd_numbers, "and the count is ", odd_count)
