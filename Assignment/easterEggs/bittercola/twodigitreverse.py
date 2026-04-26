number = int(input("Enter a positive two digit number: "))

if number >= 10 and number <= 99:
    tens_digit = number // 10
    ones_digit = number % 10
    reversed_number = (ones_digit * 10) + tens_digit

    if reversed_number > number:
        print("Reversing the digits produces a larger number")
    elif reversed_number < number:
        print("Reversing the digits produces a smaller number")
    else:
        print("Reversing the digits produces the same number")
else:
    print("Invalid input")
