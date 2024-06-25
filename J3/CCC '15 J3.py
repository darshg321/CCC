# get constanant
# find closest vowel
# add next constanant
# make substring
# append to string


word = input()

translated_word = ""

vowels = ['a', 'e', 'i', 'o', 'u']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

closest_vowel = {'b': 'a', 'c': 'a', 'd': 'e', 'f': 'e', 'g': 'e', 'h': 'i', 'j': 'i', 'k': 'i', 'l': 'i', 'm': 'o', 'n': 'o', 'p': 'o', \
    'q': 'o', 'r': 'o', 's': 'u', 't': 'u', 'v': 'u', 'w': 'u', 'x': 'u', 'y': 'u', 'z': 'u'}

for c in word:
    if c in vowels:
        translated_word += c
        continue
    
    substring = ""
    substring += c
    
    substring += closest_vowel[c]
    
    for i, cons in enumerate(consonants):
        if cons == c:
            if i == 20:
                substring += 'z'
            else: substring += consonants[i + 1]
            
    translated_word += substring
            
print(translated_word)