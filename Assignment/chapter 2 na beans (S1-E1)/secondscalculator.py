seconds = int(input("Enter number of seconds: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600

minutes = remaining_seconds // 60
seconds_remaining = remaining_seconds % 60

print(hours, "hour(s),", minutes, "minute(s),", seconds_remaining, "second(s)")
