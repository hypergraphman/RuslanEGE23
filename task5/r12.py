def f(n):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    a = [d1 * 10 + d2, d2 * 10 + d1,
         d1 * 10 + d3, d3 * 10 + d1,
         d3 * 10 + d2, d2 * 10 + d3]
    b = []
    for el in a:
        if 10 <= el <= 99:
            b.append(el)
    return max(b) - min(b)


print(f(351))
c = 0
s = 0
for i in range(100, 999 + 1):
    if f(i) == 40:
        c += 1
        s += i
        print(i)
print(c, s)