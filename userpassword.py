def strong_password(user_password):
    if len(user_password) >= 8:
        return True
    else:
        return False
        
print (strong_password("uqqqsaaaaaer"))
