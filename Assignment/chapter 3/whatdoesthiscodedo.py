'''the code prints > and < ten times in a row and also prints the nested ten times in column''' 



for row in range(10):
	for column in range(10):
		print('<' if row % 2 == 1 else '>', end='')
	print()
