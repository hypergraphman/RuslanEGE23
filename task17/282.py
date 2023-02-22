f = open('17-282.txt')
a = [int(x) for x in f.readlines()]
r = []
mn = 10**10
for el in a:
    if el < mn and el % 17 == 0:
        mn = el
for p1, p2 in zip(a, a[1:]):
    if p1 % mn == 0 or p2 % mn == 0:
        r.append(p1+p2)
print(len(r), max(r))