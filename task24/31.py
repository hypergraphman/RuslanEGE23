s = open('k7b-5.txt').read()

max_len = 0
cur_len = 0
temp = 'CA'
for p1 in s:
    if p1 == temp[cur_len % len(temp)]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    elif p1 == temp[0]:
        cur_len = 1
    else:
        cur_len = 0
print(max_len)