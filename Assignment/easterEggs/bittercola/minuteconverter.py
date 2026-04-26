total_minutes = int(input("Enter number of minutes: "))

days = total_minutes // 1440
remaining_minutes_after_days = total_minutes % 1440
hours = remaining_minutes_after_days // 60
minutes = remaining_minutes_after_days % 60

print(days, "day(s),", hours, "hour(s), and", minutes, "minute(s)")
