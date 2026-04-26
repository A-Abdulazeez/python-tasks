first_numerator = float(input("Enter first numerator: "))
first_denominator = float(input("Enter first denominator: "))
second_numerator = float(input("Enter second numerator: "))
second_denominator = float(input("Enter second denominator: "))

if first_denominator == 0 or second_denominator == 0:
    print("Denominator cannot be zero")
else:
    first_fraction = first_numerator / first_denominator
    second_fraction = second_numerator / second_denominator
    fraction_sum = first_fraction + second_fraction
    difference = first_fraction - second_fraction
    product = first_fraction * second_fraction

    print("Sum:", fraction_sum)
    print("Difference:", difference)
    print("Product:", product)

    if second_fraction == 0:
        print("Quotient cannot be calculated because division by zero is not allowed")
    else:
        quotient = first_fraction / second_fraction
        print("Quotient:", quotient)
