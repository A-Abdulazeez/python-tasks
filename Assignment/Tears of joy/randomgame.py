import random

target_number = random.randint(1, 100)
attempt_count = 0

while True:
    user_guess = int(input("Guess: "))
    attempt_count += 1

    if user_guess < target_number:
        print(user_guess, "-> higher")
    elif user_guess > target_number:
        print(user_guess, "-> lower")
    else:
        print(user_guess, "-> correct!", attempt_count, "attempts")
        break
