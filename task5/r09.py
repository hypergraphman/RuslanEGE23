def f(n):
    d1 = n // 1000
    d2 = n // 100 % 10
    d3 = n // 10 % 10
    d4 = n % 10
    # d1, d2, d3, d4 = map(int, str(n))
    a = sorted([d1 + d2, d2 + d3, d3 + d4])
    return str(a[1]) + str(a[2])


for i in range(1000, 10000):
    if f(i) == '511':
        print(i)

for n in range(1000, 10000):
    d1 = n // 1000
    d2 = n // 100 % 10
    d3 = n // 10 % 10
    d4 = n % 10
    # d1, d2, d3, d4 = map(int, str(n))
    a = sorted([d1 + d2, d2 + d3, d3 + d4])

    if str(a[1]) + str(a[2]) == '511':
        print(n)