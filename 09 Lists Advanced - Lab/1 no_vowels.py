word = input()

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

no_vowels = []

for letter in word:
    if letter not in vowels:
        no_vowels.append(letter)

filtered_word = ''.join(no_vowels)

print(filtered_word)
