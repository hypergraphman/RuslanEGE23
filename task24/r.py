s = open('24.txt').read()

max_len = 0
cur_len = 1
ans = None
for p1, p2 in zip(s, s[1:]):
    if p1 == p2:
        cur_len += 1
        if cur_len > max_len:
            ans = p1
            max_len = cur_len
    else:
        cur_len = 1
print(max_len, p1)