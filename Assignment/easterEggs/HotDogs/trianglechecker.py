side_one = float(input("Enter side 1: "))
side_two = float(input("Enter side 2: "))
side_three = float(input("Enter side 3: "))

if (side_one + side_two > side_three and side_one + side_three > side_two and side_two + side_three > side_one):
    if (side_one == side_two and side_two == side_three):
        print("The triangle is equilateral")
    elif (side_one == side_two or side_one == side_three or side_two == side_three):
        print("The triangle is isosceles")
    else:
        print("The triangle is scalene")
else:
    print("The input does not form a valid triangle")
