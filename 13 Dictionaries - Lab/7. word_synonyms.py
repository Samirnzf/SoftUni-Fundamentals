number_of_words = int(input())
word_synonyms = {}
for i in range(number_of_words):
    word = input()
    synonym = input()

    if word not in word_synonyms.keys():
        word_synonyms[word] = []
    word_synonyms[word].append(synonym)

for word in word_synonyms:
    print(f"{word} - {', '.join(word_synonyms[word])}")
