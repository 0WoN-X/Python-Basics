ip = input("Enter an IP address: ")

parts = ip.split(".")
valid = True

if len(parts) != 4:
    valid = False

for x in parts:
    if not x.isdigit():
        valid = False
    elif int(x) > 255:
        valid = False

if valid:
    print("Valid IP")
else:
    print("Invalid IP")