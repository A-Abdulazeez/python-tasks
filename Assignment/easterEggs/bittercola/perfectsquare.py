number = int(input("Enter a positive integer: "))

square_root = int(number ** 0.5)

if number > 0 and square_root * square_root == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")
