for i in range(10, 100):
    Y1 = i % 4
    Y2 = i % 2
    Y3 = i % 3
    Y = Y1 * 100 + Y2 * 10 + Y3
    if Y == 112:
        print(i)
        break
