type_of_operation = input()
first_number = int(input())
second_number = int(input())


def solution(first_number, second_number, type_of_operation):
    result = 0
    if type_of_operation == 'multiply':
        result = first_number * second_number
    elif type_of_operation == 'divide':
        result = int(first_number / second_number)
    elif type_of_operation == 'add':
        result = first_number + second_number
    elif type_of_operation == 'subtract':
        result = first_number - second_number
    return result


print(solution(first_number, second_number, type_of_operation))
