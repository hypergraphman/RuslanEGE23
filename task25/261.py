# from fnmatch import fnmatch
from re import fullmatch


k = 0
for i in range(161, 17*10**6, 161):
    # if fnmatch(str(i), '*1?*?68*'):
    if fullmatch(r'[02468]*1\d\d*\d68\d*', str(i)):
        k += 1
        if k % 500 == 1:
            print(i, i // 161)