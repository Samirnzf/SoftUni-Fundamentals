deck_of_cars = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    middle_of_the_deck = len(deck_of_cars) // 2
    left_part = deck_of_cars[:middle_of_the_deck]
    right_part = deck_of_cars[middle_of_the_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part)):
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    deck_of_cars = deck_after_shuffling
print(deck_of_cars)
