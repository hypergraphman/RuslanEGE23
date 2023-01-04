for a in range(1, 100):
    if all((y - x != 5) or (a < 2 * x ** 3 + y) or (a < y**2 + 16) for x in range(1, 100) for y in range(1, 100)):
        print(a)
