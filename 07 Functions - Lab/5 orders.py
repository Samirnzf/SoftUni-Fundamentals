ordered_item = input()
amount_of_items = int(input())


def order(ordered_item, amount_of_items):
    total_sum = 0
    if ordered_item == 'coffee':
        total_sum += 1.50 * amount_of_items
    elif ordered_item == 'coke':
        total_sum += 1.40 * amount_of_items
    elif ordered_item == 'water':
        total_sum += 1.00 * amount_of_items
    elif ordered_item == 'snacks':
        total_sum += 2.00 * amount_of_items
    return f'{total_sum:.2f}'


print(order(ordered_item, amount_of_items))



