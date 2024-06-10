name = input()
successful_sorting = True
while name != 'Welcome!':
    if name == "Voldemort":
        print("You must not speak of that name!")
        successful_sorting = False
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()

if successful_sorting: # successful_sorting == True
    print("Welcome to Hogwarts.")
