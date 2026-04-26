import random

computer_choice = random.randint(0, 2)
user_choice = int(input("Enter 0 for scissor, 1 for rock, or 2 for paper: "))

if computer_choice == 0:
    computer_name = "Scissor"
elif computer_choice == 1:
    computer_name = "Rock"
else:
    computer_name = "Paper"

if user_choice == 0:
    user_name = "Scissor"
elif user_choice == 1:
    user_name = "Rock"
elif user_choice == 2:
    user_name = "Paper"
else:
    user_name = "Invalid"

print("Computer chose:", computer_name)
print("You chose:", user_name)

if user_choice < 0 or user_choice > 2:
    print("Invalid input")
elif user_choice == computer_choice:
    print("It is a draw")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win")
else:
    print("You lose")
