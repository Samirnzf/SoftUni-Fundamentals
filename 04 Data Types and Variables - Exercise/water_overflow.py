commands = int(input())
tank_capacity = 255
for liters in range(commands):
    liters_of_water = int(input())
    if tank_capacity - liters_of_water < 0:
        print('Insufficient capacity!')
        continue
    tank_capacity -= liters_of_water
print(255 - tank_capacity)

