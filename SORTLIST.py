
numbers = [3, 1, 2, 3, 4, 1]

result = []

for number in numbers:
    if number not in result:
        result.append(number)

result.sort(reverse=True)

print(result)
