first_sequence = input().split(', ')
second_sequence = input().split(', ')
filtered_list = []

for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            filtered_list.append(first_string)
            break
print(filtered_list)

