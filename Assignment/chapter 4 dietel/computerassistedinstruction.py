import random


def generate_question():
    return random.randint(1, 9), random.randint(1, 9)


while True:
    first_number, second_number = generate_question()
    correct_answer = first_number * second_number

    while True:
        user_answer = int(input(f'How much is {first_number} times {second_number}? '))

        if user_answer == correct_answer:
            print('Very good!')
            break
        else:
            print('No. Please try again.')
