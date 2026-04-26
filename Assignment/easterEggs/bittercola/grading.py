letter_grade = input("Enter letter grade: ")

if letter_grade == "A" or letter_grade == "a":
    print("GPA value: 4.0")
elif letter_grade == "B" or letter_grade == "b":
    print("GPA value: 3.0")
elif letter_grade == "C" or letter_grade == "c":
    print("GPA value: 2.0")
elif letter_grade == "D" or letter_grade == "d":
    print("GPA value: 1.0")
elif letter_grade == "F" or letter_grade == "f":
    print("GPA value: 0.0")
else:
    print("Invalid grade")
