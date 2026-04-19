number = int(input("Enter number 1: "))
largest = number
second_largest = number

for remaining_numbers in range(2, 11):
	number = int(input(f"Enter number {remaining_numbers}: "))

	if number > largest:
		largest = number
		second_largest = largest
        
	elif number > second_largest or largest == second_largest:
		second_largest = number

print("Largest number is ", largest)
print("Second largest number is ", second_largest)