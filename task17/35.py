k = 0
mx = 0
mn = 7040
for i in range(1476, 7040):
    if i % 2 == 0 and i % 16 != 0 and i % 100 >= 40:
        k += 1
        if i > mx:
            mx = i
        if i < mn:
            mn = i
print(k,(mx+mn) // 2)