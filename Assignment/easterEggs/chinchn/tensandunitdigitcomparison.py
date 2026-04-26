number = int(input("Enter a two-digit number: "))

tens_digit = number // 10
units_digit = number % 10

if tens_digit > units_digit:
    print("The tens digit is greater than the units digit")
elif tens_digit < units_digit:
    print("The tens digit is less than the units digit")
else:
    print("The tens digit is equal to the units digit")
