filename = input("Enter the log file name: ")

file = open(filename, "r")

for line in file:
    if "ERROR" in line:
        print(line)

file.close()