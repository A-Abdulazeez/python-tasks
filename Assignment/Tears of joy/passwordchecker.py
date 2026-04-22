correct_password = "python123"
attempts = 0

for password in range (3):
    password = input("Password: ")

    if password == correct_password:
        print("Access granted")
        break

    attempts += 1

    if attempts == 3:
        print("Locked out")
