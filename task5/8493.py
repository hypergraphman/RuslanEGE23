for n in range(0,100):
    n1 = bin(n)[2:]
    if n % 3 == 0:
        n2 = n1 + n1[-3:]
    else:
        n2 = n1 + bin(n % 3 * 3)[2:]
    if int(n2, 2) < 76:
        print(n)