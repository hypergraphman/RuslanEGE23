from itertools import product

k = 0
for word in product('0123456', repeat=6):
    word = ''.join(word)
    if word[0] != '0' and word.count('6') == 1 and (
             word[0] in '0246' and word[2] in '0246' and word[4] in '0246' and
             word[1] in '135' and word[3] in '135' and word[5] in '135' or
             word[1] in '0246' and word[3] in '0246' and word[5] in '0246' and
             word[0] in '135' and word[2] in '135' and word[4] in '135'
    ):
        k += 1
print(k)