number_of_strings = int(input())

for strings in range(number_of_strings):
    string = input()
    flag = False
    for i in string:
        if i in (',', '.', '_'):
            print(f'{string} is not pure!')
            flag = True
            break
    if not flag:
        print(f'{string} is pure.')
