list_of_numbers = input().split()

rounded = []

for number in list_of_numbers:
    rounded.append(round(float(number)))

print(rounded)
