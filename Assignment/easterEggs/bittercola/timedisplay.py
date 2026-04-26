first_hour = int(input("Enter first time hour: "))
first_minute = int(input("Enter first time minute: "))
second_hour = int(input("Enter second time hour: "))
second_minute = int(input("Enter second time minute: "))

total_minutes = first_minute + second_minute
extra_hours = total_minutes // 60
final_minutes = total_minutes % 60
final_hours = first_hour + second_hour + extra_hours

print("Total time:", final_hours, "hour(s) and", final_minutes, "minute(s)")
