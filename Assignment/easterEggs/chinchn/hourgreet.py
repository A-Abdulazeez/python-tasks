current_hour = int(input("Enter current hour from 0 to 23: "))

if current_hour >= 5 and current_hour <= 11:
    print("Good Morning")
elif current_hour >= 12 and current_hour <= 17:
    print("Good Afternoon")
elif current_hour >= 18 and current_hour <= 21:
    print("Good Evening")
elif (current_hour >= 22 and current_hour <= 23) or (current_hour >= 0 and current_hour <= 4):
    print("Good Night")
else:
    print("Invalid hour")
