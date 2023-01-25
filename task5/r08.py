for n in range(1, 100):
    s1 = bin(n)[2:]
    s2 = s1 + str(sum(map(int, s1)) % 2)
    s3 = s2 + '0'
    r = int(s3, 2)

    if r > 137:
        print(n)



