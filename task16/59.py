def f(n):
    if n > 30:
        return n * n + 5 * n + 4
    elif n <= 30 and n % 2 == 0:
        return f(n + 1) + 3 * f(n + 4)
    elif n <= 30 and n % 2 != 0:
        return 2 * f(n + 2) + f(n + 5)


x = 0
for i in range(0, 1001):
    if sum(map(int, str(f(i)))) == 27:
        x = x + 1
print(x)