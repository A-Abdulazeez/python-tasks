first_edge = float(input("Enter first edge: "))
second_edge = float(input("Enter second edge: "))

if first_edge > 0 and second_edge > 0 and first_edge != second_edge:
    perimeter = 2 * (first_edge + second_edge)
    print("Perimeter is", perimeter)
else:
    print("Invalid rectangle edges")
