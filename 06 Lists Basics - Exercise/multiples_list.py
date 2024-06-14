factor = int(input())
count_of_numbers = int(input())
multiples_list = []
for number in range(1, count_of_numbers + 1):
    if factor > 0:
        multiples_list.append(factor * number)
print(multiples_list)
