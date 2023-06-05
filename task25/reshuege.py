def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


for x in range(2422000, 2422080 + 1):
    if len(divs(x)) == 2:
        print(x)