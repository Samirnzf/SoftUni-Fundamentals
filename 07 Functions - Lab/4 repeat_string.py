word = input()
number_of_repeats = int(input())

repeat_string = lambda word, number_of_repeats: word * number_of_repeats
result = repeat_string(word, number_of_repeats)
print(result)


#def repeat_string(word, number_of_repeats):
    #return word * number_of_repeats