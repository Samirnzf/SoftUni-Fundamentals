number_of_characters = int(input())
total_sum = 0
for character in range(number_of_characters):
    char = input()
    total_sum += ord(char)

print(f'The sum equals: {total_sum}')


