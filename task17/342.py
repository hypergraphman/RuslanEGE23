f = open('17-342.txt')
a = [int(x) for x in f.readlines()]
mn37 = 10**10
for el in a:
    if el < mn37 and el % 37 == 0:
        mn37 = el
# mn37 = min(filter(key=lambda x: x % 37 == 0, a))
mx73 = 0
for el in a:
    if el > mx73 and el % 73 == 0:
        mx73 = el
# mx73 = max(filter(key=lambda x: x % 73 == 0, a))
# print(mx73, mn37)
r = []
for p1, p2 in zip(a, a[1:]):
    if (mx73 < p1 < mn37 and not (mx73 < p2 < mn37) or
       mx73 < p2 < mn37 and not (mx73 < p1 < mn37)):
        r.append(p1 + p2)
print(len(r), min(r))