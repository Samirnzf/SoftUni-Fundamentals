numbers = []

for number in range(3):
    current_number = int(input())
    numbers.append(current_number)


def smallest(numbers):
    smallest = min(numbers)
    return smallest


print(smallest(numbers))
