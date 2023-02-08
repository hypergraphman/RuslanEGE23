def divs(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


print(len(divs(121)))

i = 117
c = 0
while len(divs(i)) != 2:
    i += 4
    c += 1
print(i, c)