list_with_numbers = input().split()
opposite_numbers = []
for current_number in list_with_numbers:
    opposite_number = -int(current_number)
    opposite_numbers.append(opposite_number)
print(opposite_numbers)

# print([-int(number) for number in input().split()]