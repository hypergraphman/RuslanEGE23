def f(x):
    return x % 2 * 100 + x % 3 * 10 + x % 5


for i in range(10, 100):
    if f(i) == 104:
        print(i)

i = 10
while f(i) != 104:
    i += 1
print(i)