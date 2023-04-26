from fnmatch import fnmatch

k = 0
for i in range(161, 17*10**6, 161):
    if fnmatch(str(i), '*1?*?68*'):
        k += 1
        if k % 500 == 1:
            print(i, i // 161)