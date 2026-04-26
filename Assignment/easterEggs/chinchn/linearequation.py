a_coefficient = float(input("Enter a: "))
b_coefficient = float(input("Enter b: "))
c_coefficient = float(input("Enter c: "))

if a_coefficient == 0:
    print("The equation has no unique solution")
else:
    solution_x = (c_coefficient - b_coefficient) / a_coefficient
    print("x is", solution_x)
