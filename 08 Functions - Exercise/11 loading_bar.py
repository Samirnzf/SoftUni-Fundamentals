def generate_loading_bar(number):
    filled_blocks = number // 10

    empty_blocks = 10 - filled_blocks

    loading_bar = '[' + '%' * filled_blocks + '.' * empty_blocks + ']'

    return loading_bar


input_number = int(input())

if input_number == 100:
    print(f'{input_number}% Complete!')
    print(generate_loading_bar(input_number))
else:
    print(f'{input_number}% {generate_loading_bar(input_number)}')
    print('Still loading...')
