
path = input("Enter a file path: ")

if "../" in path or "..\\" in path:
    print("404 ....!")
else:
    print("Safe path. ")

