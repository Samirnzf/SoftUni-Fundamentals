lost_fights_counter = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet_counter = 0
broken_sword_counter = 0
broken_shield_counter = 0
broken_armor_counter = 0

for lost_fight in range(1, lost_fights_counter + 1):
    if lost_fight % 2 == 0:
        broken_helmet_counter += 1
    if lost_fight % 3 == 0:
        broken_sword_counter += 1
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        broken_shield_counter += 1
        if broken_shield_counter % 2 == 0:
            broken_armor_counter += 1

helmet_repair_price = helmet_price * broken_helmet_counter
sword_repair_price = sword_price * broken_sword_counter
shield_repair_price = shield_price * broken_shield_counter
armor_repair_price = armor_price * broken_armor_counter

total_repair_price = helmet_repair_price + sword_repair_price + \
    shield_repair_price + armor_repair_price

print(f'Gladiator expenses: {total_repair_price:.2f} aureus')
