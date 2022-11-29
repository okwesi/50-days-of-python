

def convert_add(numbers):
	return sum(list(map(int, numbers)))

print(convert_add(['1', '3', '5']))


def check_duplicates(_list):
	duplicates = []
	unique = []
	for value in _list:
		if value not in unique:
			unique.append(value)
		else:
			duplicates.append(value)
	if len(duplicates) == 0:
		return "No duplicates"
	else:
		return "Duplicates"

print(check_duplicates(['apple', 'orange', 'banana', 'apple']))