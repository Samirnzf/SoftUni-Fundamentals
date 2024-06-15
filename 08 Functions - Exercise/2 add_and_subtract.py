###third_number = int(input())


# def add_and_subtract(first_number, second_number, third_number):
# return first_number + second_number - third_number


# print(add_and_subtract(first_number, second_number, third_number))


add_numbers = []

for number in range(2):
    current_number = int(input())
    add_numbers.append(current_number)

subtract_number = int(input())


def add_and_subtract(add_numbers, subtract_number):
    return sum(add_numbers) - subtract_number


print(add_and_subtract(add_numbers, subtract_number))
