for i in range(1, 100):
    s1 = bin(i)[2:]
    s2a = s1 + str(sum(map(int, s1)) % 2)
    s3b = s2a + '0'
    if int(s3b, 2) > 43:
        print(int(s3b, 2))
        break
