#SQL INJECTION :


text = input("Enter a string: ")

if "--" in text or ";" in text or "' OR '1'='1" in text.upper():
    print("SQL injection detected!")
else:
    print("No SQLI detected.") 