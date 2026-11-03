malicious_ips = ["185.10.20.30", "45.67.89.10", "192.168.2.5"]

ip = input("Enter an IP address: ")

if ip in malicious_ips:
    print("Warning! This IP address is malicious.")
else:
    print("This IP address is not in the malicious list.")