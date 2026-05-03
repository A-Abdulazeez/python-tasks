def naira_exchange(dollar_amount):
	if type (dollar_amount) != float and type (dollar_amount) != int:
		return"invalid input"
	result = dollar_amount * 1550
	return result
	
print (naira_exchange(1.2))
