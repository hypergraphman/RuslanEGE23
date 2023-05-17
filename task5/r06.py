for n in range(1000, 10000):
    a, b, c, d = n // 1000, n // 100 % 10, n // 10 % 10, n % 10
    s = sorted([a + b, c + d], reverse=True)
    r = ''.join(map(str, s))
    if r == '1311':
        print(n)
        break

