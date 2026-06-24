import time

# Correct password
correct_password = "Admin@123"

# Maximum attempts
max_attempts = 3

attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Incorrect password! Attempts remaining: {remaining}")

if attempts == max_attempts:
    print("\nToo many failed attempts!")
    print("Account locked for 10 seconds...")

    time.sleep(10)

    print("You may try again later.")