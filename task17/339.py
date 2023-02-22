f = open('17-339.txt')
a = [int(x) for x in f.readlines()]
r = []
mn = 10**10
for el in a:
    if el > 0 and el % 19 == 0 and el < mn:
        mn = el
for p1, p2 in zip(a, a[1:]):
    if p1 + p2 < mn:
        r.append(p1 + p2)
print(len(r), abs(max(r)))