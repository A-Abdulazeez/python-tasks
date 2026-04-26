a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    root_one = (-b + (discriminant ** 0.5)) / (2 * a)
    root_two = (-b - (discriminant ** 0.5)) / (2 * a)
    print("The roots are", root_one, "and", root_two)
elif discriminant == 0:
    root = -b / (2 * a)
    print("The root is", root)
else:
    print("The equation has no real roots")
