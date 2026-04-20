print(f"{"Multiplication Table":^35}")


for number in range (1,10):
	print(number, end="|")
	for number_across in range (1,10):
		multiplication = number * number_across
		print(f"{multiplication:>2}", end="  ")
	print()
