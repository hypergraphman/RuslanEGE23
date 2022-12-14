def n_to_p(n, p):
    r = ''
    digs = '0123456789ABCDEF'
    while n > 0:
        r = digs[n % p] + r
        n = n // p
    return r


print(n_to_p(64**10 + 2**90 - 16, 8).count('7'))