number = int(input("Enter a four-digit integer: "))

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
units_digit = number % 10

print("Reverse order:", units_digit, tens_digit, hundreds_digit, thousands_digit, sep="")
