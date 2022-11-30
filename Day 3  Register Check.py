
def register_check(register):
	values = list(register.values())
	return values.count("yes")

register = {'Michael':'yes','John': 'no', 
 'Peter':'yes', 'Mary': 'yes'}

print(register_check(register))



def lower_case(names):
	tup = []
	for name in names:
		if name.islower():
			tup.append(name)
	return tuple(tup)

names = ["kerry", "dickson", "John", "Mary", 
 "carol", "Rose", "adam"]
print(lower_case(names))