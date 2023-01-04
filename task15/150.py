for a in range(1, 1000):
    if all((x & 56 != 0) <= ((x & 48 == 0) <= (x & a != 0)) for x in range(0, 100)):
        print(a)
        break
