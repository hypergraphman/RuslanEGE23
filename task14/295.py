def n_to_p(n,p):
    r = ''
    alf = '0123456789'
    while n > 0 :
        r = alf[n % p] + r
        n = n//p
    return r


print(n_to_p(6**203 + 5 * 6**405 - 3 * 6**144 + 77,6).count('5'))