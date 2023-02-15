f = open('17-338.txt')
# a = []
# for line in f.readlines():
#     n = int(line)
#     a.append(n)
a = [int(x) for x in f.readlines()]
# mn = 10**10
# for el in a:
#     if el < mn:
#         mn = el
mn = min(a)
r = []
# r = [p1 + p2 for p1, p2 in zip(a, a[1:]) if p1 % 117 == mn or p2 % 117 == mn]
for p1, p2 in zip(a, a[1:]):
    if p1 % 117 == mn or p2 % 117 == mn:
        r.append(p1 + p2)
print(len(r), max(r))