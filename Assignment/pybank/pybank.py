def user_email(user_email):
	if user_email[0] == "@" or user_email[-1] == "@":
		return "invalid email"
	if "@" not in user_email:
		return False
	if len(user_email) <= 8:
        	return False
	if len(user_email) > 8:
		return True
	


def calculate_balance(transactions):
    balance = 0
    for transaction in transactions:
        balance += transaction
    return balance       


def strong_password(user_password):
    if len(user_password) >= 8:
        return True
    else:
        return False
        
        
def apply_interest(balance,rate, years):
	if rate < 0 or years < 1:
		return False
	else:
        	return True
		#raise ValueError ("invalid")
	compound_interest = balance *((1+rate) ** years)
	return round(compound_interest,2)
	
def get_transaction_summary(transactions):
    total_credits = 0
    total_debits = 0
    net_balance = 0
    transaction_count = 0
    
    for transaction in transactions:
        if transaction[0] == "credit":
            total_credits += transaction[1]
        else:
            total_debits += transaction[1]
            
        transaction_count += 1
        
    net_balance = total_credits - total_debits
    
    return [["total_credits", total_credits], ["total_debits", total_debits], ["net_balance", net_balance], ["transaction_count", transaction_count]]

        
