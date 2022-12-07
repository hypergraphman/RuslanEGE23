from itertools import product

alf = 'видео'
words = set()
for letters in product(alf, repeat=6):
    vowels = [letter for letter in letters if letter in 'иео']
    if (letters.count('и') >= 1 and letters.count('е') >= 1 and
       vowels == sorted(vowels)):
        words.add(letters)
print(len(words))