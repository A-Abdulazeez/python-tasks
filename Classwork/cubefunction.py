def cube(number):
	if type (number) != int:
		return"invalid input"
	result = number ** 3
	return result
	
print(cube(10))
