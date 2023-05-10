s = open('k7-m7.txt').read()

k = 0
for p1 in s:
    if p1 == 'C':
        k += 1
# print(k, s.count('C'))

cur_len = 0
data = []
for p1 in s:
    if p1 == 'C':
        cur_len += 1
    elif cur_len > 0:
        data.append(cur_len)
        cur_len = 0
if cur_len > 0:
    data.append(cur_len)
# print(data)

p = 1
for el in data:
    p = p * el
# print(p)

s1 = s.replace('C','')
s2 = str(k) + 'C' * k + str(p) + s1
print(len(data))
print(s[:35])
print(s2[:35])