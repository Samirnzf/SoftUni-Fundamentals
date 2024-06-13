number_of_snowballs = int(input())
max_weight = int(input())
max_time = int(input())
max_quality = int(input())
max_value = (max_weight / max_time) ** max_quality
for current_snowball in range(number_of_snowballs - 1):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality
    if current_value > max_value:
        max_value = current_value
        max_weight = current_weight
        max_time = current_time
        max_quality = current_quality
print(f'{max_weight} : {max_time} = {int(max_value)} ({max_quality})')
