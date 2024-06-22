products_and_quantities = input().split()
products_in_stock = dict()
for index in range(0, len(products_and_quantities), 2):
    product = products_and_quantities[index]
    quantity = int(products_and_quantities[index + 1])
    products_in_stock[product] = quantity

searching_for = input().split()

for item in searching_for:
    if item not in products_in_stock:
        print(f"Sorry, we don't have {item}")
    elif item in products_in_stock:
        print(f"We have {products_in_stock[item]} of {item} left")
