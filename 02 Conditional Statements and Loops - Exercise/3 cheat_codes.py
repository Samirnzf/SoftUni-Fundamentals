number_of_codes = int(input())

for _ in range(number_of_codes):
    cheat_code = int(input())
    if cheat_code == 88:
        print('Hello')
    elif cheat_code == 86:
        print('How are you?')
    elif cheat_code < 88:
        print('GREAT!')
    else:
        print('Bye.')
