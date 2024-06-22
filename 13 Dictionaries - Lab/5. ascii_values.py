list_of_characters = input().split(', ')
dictionary = {}
for character in list_of_characters:
    dictionary[character] = dictionary.get(character, ord(character))
print(dictionary)
