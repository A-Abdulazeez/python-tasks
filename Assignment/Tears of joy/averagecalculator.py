total = 0
count = 0
    
while True:
	user_number = int(input("Enter your number: "))
	
	if user_number == -1:
            break

	total += user_number
	count += 1

if count > 0:
        average = total / count
        print(f"Average is:  {average}")
else:
        print("nawa ooooo")
