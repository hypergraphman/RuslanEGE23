f = open('17-1.txt')
a = [int(x) for x  in f.readlines()]
r = []
for p1, p2 in zip(a, a[1:]):
    if p1 % 7 == 0 and p2 % 17 != 0 or p1 % 17 != 0 and p2 % 7 == 0:
        r.append(p1 + p2)
print(len(r), min(r))