for i in range(1, 100):
    s1 = bin(i)[2:]
    if sum(map(int, s1)) % 2 == 0:
        s2 = '10' + s1[2:] + '0'
    else:
        s2 = '11' + s1[2:] + '1'
    if int(s2, 2) > 40:
        print(i)
        break