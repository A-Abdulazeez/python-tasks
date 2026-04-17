''' create an input to collect the password'
count the number of the password to know the length 
use if statement to decide the weak,strong,and very strong''' 







password = input("Create your password: ")
password_strength = len(password)

if (password_strength < 8):
	print("your password is weak")
 
elif (password_strength >= 8 and password_strength < 16):
	print("your password is strong")
	
elif (password_strength > 16):
	print("your password is very strong")
