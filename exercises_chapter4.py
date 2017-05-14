import nltk, re, pprint

# #######################
# # 4.2 Tuples and Lists
# #######################

# def sequence_operations(list_or_tuple):
#     print('Sequenz:', list_or_tuple)
#     print('Sortierte Sequenz:', sorted(list_or_tuple))
#     print('Umgekehrte Reihenfolge', [x for x in reversed(list_or_tuple)])
#     print('Sequenz hat die Länge:', len(list_or_tuple))
#     print('Vereinen zweier Sequenzen', list_or_tuple + list_or_tuple)
#     print('Multiplizieren einer Sequenz:', list_or_tuple * 3)
#     print('4 appears', list.count(4), 'times')
#
#
# list = [4, 8, 2]
# tuple = (4, 8, 2)
# sequence_operations(list)
# sequence_operations(tuple)

# def list_operations(list):
#     list.append(6)
#     print('Element was adden:', list)
#     list.pop()
#     print('Last element was removed:', list)
#     list.remove(8)
#     print('Specific elment was removed:', list)
#
# list = [4, 8, 2]
# list_operations(list)
# #######################


# ###########################
# # 4.10 Sort Words by Length
# ###########################

# def sort_words_by_length(words):
#     word_length = [(len(word), word) for word in words]
#     sorted_words = sorted(word_length)
#     sorted_words = [word for (_, word) in sorted_words]
#     return sorted_words
#
# words = ['Das', 'ist', 'das', 'Haus', 'vom', 'Nikolaus']
# print(sort_words_by_length(words))

# ###########################


# #######################################
# # 4.13 Word Length and Number of Vowels
# #######################################

# Write code to initialize a two-dimensional array of sets called word_vowels and process a list of words,
# adding each word to word_vowels[l][v] where l is the length of the word and v is the number of vowels it contains.

def word_length_vowels(words):
    word_length_vowels = [(len(word), len(re.sub(r'[^aeiou]', '', word)), word) for word in words]
    vowel_arrs = [[] for _ in range(max(x[1] for x in word_length_vowels)+1)]
    num_of_length = len(set([x[0] for x in word_length_vowels]))
    word_vowels = [vowel_arrs for _ in range(num_of_length)]
    word_vowels.append(vowel_arrs)

    for length, vowels, word in word_length_vowels:
        word_vowels[length][vowels].append(word)
    return word_vowels


words = nltk.corpus.brown.words(categories=['hobbies'])
print(words[100:115])
print(word_length_vowels(words[100:115]))

# #######################################