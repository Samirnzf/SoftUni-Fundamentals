extracted_word = input()
text = input()

while extracted_word in text:
    text = text.replace(extracted_word, '')
print(text)
