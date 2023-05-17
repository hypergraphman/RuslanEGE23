for n in range(1, 999):
    s1 = bin(n)[2:]
    if s1.count('1') % 2 == 0:
        s2a = s1 + '0'
    else:
        s2a = s1 + '1'
    s2b = s2a + '0'
    if int(s2b, 2) > 43:
        print(int(s2b, 2))
        break