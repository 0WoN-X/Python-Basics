
message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))

encrypted = ""

for letter in message:
    if letter.isalpha():
        number = ord(letter) + shift

        if letter.islower():
            if number > ord('z'):
                number = number - 26
        else:
            if number > ord('Z'):
                number = number - 26

        encrypted = encrypted + chr(number)
    else:
        encrypted = encrypted + letter

print("Encrypted message:", encrypted)
