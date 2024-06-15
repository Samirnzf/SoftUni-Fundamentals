def get_sorted_numbers(numbers):
    numbers = list(map(int, numbers.split()))

    sorted_numbers = sorted(numbers)

    return sorted_numbers


numbers_input = input()

sorted_numbers_list = get_sorted_numbers(numbers_input)

print(sorted_numbers_list)