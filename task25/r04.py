# from fnmatch import fnmatch
#
# for i in range(2023, 10**10, 2023):
#     if fnmatch(str(i), '1?2139*4'):
#         print(i, i // 2023)
#
#
# from re import fullmatch
#
# for i in range(2023, 10**10, 2023):
#     if fullmatch(r'1\d2139\d*4', str(i)):
#         print(i, i // 2023)

res = []
for x in range(10):
    for y in [''] + list(range(0, 1000)):
        s = f'1{x}2139{y}4'
        t = int(s)
        if t % 2023 == 0:
            res.append((t, t // 2023))
res.sort()
print(res)