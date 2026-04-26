years = int(input("Enter the number of years: "))

current_population = 312032486

seconds_in_year = 365 * 24 * 60 * 60

births_per_year = seconds_in_year // 7
deaths_per_year = seconds_in_year // 13
immigrants_per_year = seconds_in_year // 45

population = current_population + years * (births_per_year + immigrants_per_year - deaths_per_year)

print("The population in", years, "years is", population)
