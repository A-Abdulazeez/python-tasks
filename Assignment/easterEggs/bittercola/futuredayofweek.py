days_from_today = int(input("Enter number of days from today: "))

day_number = days_from_today % 7

if day_number == 0:
    print("Monday")
elif day_number == 1:
    print("Tuesday")
elif day_number == 2:
    print("Wednesday")
elif day_number == 3:
    print("Thursday")
elif day_number == 4:
    print("Friday")
elif day_number == 5:
    print("Saturday")
elif day_number == 6:
    print("Sunday")
