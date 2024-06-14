number_of_inputs = int(input())
list_of_positives = []
list_of_negatives = []
count_of_positives = 0
sum_of_negatives = 0

for number in range(number_of_inputs):
    command = int(input())
    if command > 0:
        list_of_positives.append(command)
        count_of_positives += 1
    elif command < 0:
        list_of_negatives.append(command)
        sum_of_negatives += command
print(list_of_positives)
print(list_of_negatives)
print(f'Count of positives: {count_of_positives}')
print(f'Sum of negatives: {sum_of_negatives}')
