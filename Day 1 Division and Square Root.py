import math

def divide_or_square(number):
	if number % 5 == 0:
		return math.sqrt(number)
	else:
		return number % 5


def longest_value(dict): 
	return max(dict.values(), key=len)

divide_or_square(11))
longest_value({'fruit': 'apple', 'color': 'green'}))