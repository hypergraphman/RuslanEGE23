def n_to_p(n, p):
    r = ''
    digs = '0123456789ABCDEF'
    while n > 0:
        r = digs[n % p] + r
        n = n // p
    return r


q = n_to_p(7**103 * 6 * 7**104 -3 * 7**57 + 98, 7)
s = 0
for el in q:
    s = s + int(el)
print(s)
print(sum(map(int, q)))