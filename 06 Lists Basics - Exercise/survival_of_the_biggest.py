list_of_numbers = input().split(' ')
numbers = []

for number in list_of_numbers:
    numbers.append(int(number))

numbers_to_remove = int(input())

for i in range(numbers_to_remove):
    lowest_numbers = min(numbers)
    numbers.remove(lowest_numbers)

print(*numbers, sep=", ")
