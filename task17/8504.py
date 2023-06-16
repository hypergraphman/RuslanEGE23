f = open('17_8504.txt')
a = []
mn = float('inf')
for el in f.readlines():
    a.append(int(el))
    if a[-1] < mn and 100 <= a[-1] < 1000:
        mn = a[-1]
r = []
for p1, p2 in zip(a, a[1:]):
    if (100 <= p1 < 1000 or 100 <= p2 < 1000) and (p1 + p2) % mn == 0:
        r.append(p1 + p2)
print(len(r), max(r))