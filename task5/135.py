q = 0
for i in range(1, 100):
    s1 = bin(i)[2:]
    s2 = s1 + '10'[sum(map(int, s1)) % 2]
    s3 = s2 + '10'[sum(map(int, s2)) % 2]
    if 16 <= int(s3, 2) <= 32:
        q += 1
print(q)
