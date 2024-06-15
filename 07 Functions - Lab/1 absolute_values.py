numbers = input().split(' ')
filtered_list = []


def absolute_values(numbers):
    for number in numbers:
        filtered_list.append(abs(float(number)))
    return filtered_list


print(absolute_values(numbers))
