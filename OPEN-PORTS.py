
open_ports = [22, 80, 443, 3306, 8080]

start = int(input("Enter the starting port: "))
end = int(input("Enter the ending port: "))

print("Open ports:")

for port in range(start, end + 1):
    if port in open_ports:
        print(port, "is open")

