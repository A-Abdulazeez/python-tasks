import random


def play_game():
    number = random.randint(1, 1000)
    user_guess = int(input('guess my number between 1 and 1000: '))

    while user_guess != number:
        if user_guess > number:
            print('Too high. Try again.')
        else:
            print('Too low. Try again.')
        user_guess = int(input('Enter your next guess: '))

    print('Congratulations. You guessed the number!')


while True:
    play_game()
    again = input('Do you want to play again? (yes or no): ').lower()
    if again != 'yes':
        break
