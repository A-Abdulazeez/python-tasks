day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

is_leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
maximum_day = 0

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    maximum_day = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    maximum_day = 30
elif month == 2:
    if is_leap_year:
        maximum_day = 29
    else:
        maximum_day = 28

if year > 0 and month >= 1 and month <= 12 and day >= 1 and day <= maximum_day:
    print("Valid date")
else:
    print("Invalid date")
