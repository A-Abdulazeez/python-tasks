while True:
    student_name = input("Student name: ")

    if student_name == "":
        break

    total = 0
    count = 0

    while True:
        student_score = int(input("Score: "))

        if student_score == -1:
            break

        total += student_score
        count += 1

    if count > 0:
        average = total / count
        print(f"{student_name} avg: {average}")
    else:
        print(f"{student_name} has no scores")
