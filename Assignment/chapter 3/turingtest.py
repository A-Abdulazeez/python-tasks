user_problem = input("What is your problem? ",)

previous_experience = input("Have you had this problem before (yes or no)? ")

if (previous_experience == "yes"):
	print("Well, you have it again")
elif (previous_experience == "no"):
	print("Well, you have it now")



'''this wont convince the user that the code has exhibited intelligent behaviour, because it ignored the first user problem and just jumped to asking about their previous experience without diagnozing the first asked problem. and then after asking for previous experience it just jumped to you have it again if user input is yes and you have it now if user input is no. so this diagnosis block of code wont convince the user that it's intelligent'''
