s = open('24.txt').read()

max_len = 0
cur_len = 0
for p1 in s:
    if p1 == 'C':
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0
print(max_len)