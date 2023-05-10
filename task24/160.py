from collections import Counter

f = open('24-s1.txt')
lines = f.readlines()
min_line = None
mn = float('inf')
for line in lines:
    if line.count('A') < mn:
        mn = line.count('A')
        min_line = line
schetchik = Counter(min_line)

find = sorted(schetchik.items(), key=lambda x: (-x[1], -ord(x[0])))[0][0]
k = 0
for line in lines:
    k += line.count(find)
print(find + str(k))