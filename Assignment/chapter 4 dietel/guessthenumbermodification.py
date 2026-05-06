import random


def play_game():
    number = random.randint(1, 1000)
    guess_count = 0

    while True:
        guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))
        guess_count += 1

        if guess == number:
            print('Congratulations. You guessed the number!')
            if guess_count <= 10:
                print('Either you know the secret or you got lucky!')
            else:
                print('You should be able to do better!')
            break
        elif guess > number:
            print('Too high. Try again.')
        else:
            print('Too low. Try again.')


while True:
    play_game()
    again = input('Do you want to play again? (yes or no): ').lower()
    if again != 'yes':
        break

