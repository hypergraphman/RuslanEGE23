c = 0
for a in range(0, 1000):
    if all(((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y < 10)) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        c += 1
print(c)
