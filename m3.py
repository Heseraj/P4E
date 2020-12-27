
def square(x):
	y = x * x
	return y

def greater_than (x, y):
	if x < y:
		return True
	else:
		return False

def absolute_value(x):
	if x >= 0:
		return x
	else:
		return -1 * x




num_list = [-10, 5, 0.5, -0.5, 12, 5, 7]

for i in num_list:
	result = greater_than[num_list[i]]
print(result)


def f_to_c(t):
	return (t - 32) * 5.0 / 9.0

def print_c_from_f():
	f = int(input("What is the temprature today? "))
	c = f_to_c(f)
	print(c)

def greet():
	name = input("what is your name?")
	print("Hello", name, "Good Morning!")
