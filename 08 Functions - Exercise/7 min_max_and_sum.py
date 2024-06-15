def min_max_and_sum(numbers):
    numbers = list(map(int, numbers.split()))

    min_value = min(numbers)

    max_value = max(numbers)

    sum_value = sum(numbers)

    return min_value, max_value, sum_value


numbers_input = input()

min_value, max_value, sum_value = min_max_and_sum(numbers_input)

print("The minimum number is", min_value)
print("The maximum number is", max_value)
print("The sum number is:", sum_value)
