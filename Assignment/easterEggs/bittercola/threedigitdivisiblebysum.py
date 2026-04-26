number = int(input("Enter a 3-digit number: "))

if number >= 100 and number <= 999:
    hundreds_digit = number // 100
    tens_digit = (number // 10) % 10
    ones_digit = number % 10
    digit_sum = hundreds_digit + tens_digit + ones_digit

    if number % digit_sum == 0:
        print(number, "is divisible by the sum of its digits")
    else:
        print(number, "is not divisible by the sum of its digits")
else:
    print("Invalid input. Enter a 3-digit integer.")
