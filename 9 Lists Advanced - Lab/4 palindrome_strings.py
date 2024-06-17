words = input().split()
searched_palindrome = input()

list_of_palindromes = [word for word in words if word == ''.join(reversed(word))]

print(f'{list_of_palindromes}')
print(f'Found palindrome {list_of_palindromes.count(searched_palindrome)} times')
