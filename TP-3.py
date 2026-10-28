port = int(input("Enter port number: "))

if port < 0 or port > 65535:
    print("Invalid port number")

elif port <= 1023:
    print("Well-known port")

elif port <= 49151:
    print("Registered port")

else:
    print("Dynamic / Private port")