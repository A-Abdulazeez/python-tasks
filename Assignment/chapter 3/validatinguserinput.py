'''Initialize passes to zero
Initialize failures to zero
Initialize count to zero
if result is not equal to one or two coutinue
For each of the ten students
Input the next exam result
If the student passed
Add one to passes
Else
Add one to failures
Display the number of passes
Display the number of failures
If more than eight students passed 
Display “Bonus to instructor" '''


#pseudocode come hard pass the code itself








passes = 0
failures = 0
count = 0

while count < 10:
	result = int(input("Enter result (1=pass, 2=fail): "))
	if result != 1 and result != 2:
		continue
		
	if (result == 1):
		passes = passes + 1
		print("You passed")
	elif (result == 2):
		failures = failures + 1
		print("you failed")
	count += 1
	
print("passed: ", passes)
print("failed: ", failures)

if passes > 8:
	print("Bonus to instructor")
			
	
