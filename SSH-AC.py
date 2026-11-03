username = input("Enter username: ")
password = input("Enter password: ")

if username == "root":
    print("Access denied: root login is not allowed.")
elif len(password) < 12:
    print("Access denied: password must be at least 12 characters.")
else:
    print("SSH access granted!")