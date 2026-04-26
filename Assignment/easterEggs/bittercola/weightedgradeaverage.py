first_score = float(input("Enter first exam score: "))
second_score = float(input("Enter second exam score: "))
third_score = float(input("Enter third exam score: "))

highest_score = first_score
middle_score = second_score
lowest_score = third_score

if highest_score < middle_score:
    temporary_score = highest_score
    highest_score = middle_score
    middle_score = temporary_score

if highest_score < lowest_score:
    temporary_score = highest_score
    highest_score = lowest_score
    lowest_score = temporary_score

if middle_score < lowest_score:
    temporary_score = middle_score
    middle_score = lowest_score
    lowest_score = temporary_score

weighted_average = (highest_score * 0.40) + (middle_score * 0.35) + (lowest_score * 0.25)

print("Weighted average:", weighted_average)
