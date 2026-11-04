
from datetime import datetime, timedelta

failed_attempts = []

while True:
    username = input("Enter username: ")

    if len(failed_attempts) >= 3:
        first_attempt = failed_attempts[0]
        current_time = datetime.now()

        if current_time - first_attempt < timedelta(minutes=10):
            print("Login blocked.")
            break
        else:
            failed_attempts = []

    password = input("Enter password: ")

    if username == "admin" and password == "password123":
        print("Login successful!")
        break
    else:
        print("Login failed!")

        failed_attempts.append(datetime.now())

        print("Failed attempts:", len(failed_attempts))
