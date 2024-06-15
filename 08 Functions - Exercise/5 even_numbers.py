def get_even_numbers(numbers):
    numbers = list(map(int, numbers.split()))

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    return even_numbers


numbers_input = input()

even_numbers_list = get_even_numbers(numbers_input)


print(even_numbers_list)
