minutes = int(input("Enter the number of minutes: "))

minutes_in_year = 365 * 24 * 60
years = minutes // minutes_in_year

remaining_minutes = minutes % minutes_in_year
days = remaining_minutes // (24 * 60)

print(minutes, "minutes is approximately", years, "years and", days, "days")
