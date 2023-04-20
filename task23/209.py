def f(s, e, k):
    if s == e and k % 2 != 0:
        return 1
    if s > e:
        return 0
    return f(s + 2, e, k + 1) + f(s * 2, e, k + 1) + f(s**2, e, k + 1)


print(f(1, 100, 0))
a = [0] * 101
a[1] = 1
for i in range(1, 100):
    if i + 2 <= 100:
        a[i + 2] += a[i]
    if i * 2 <= 100:
        a[i * 2] += a[i]
    if i ** 2 <= 100:
        a[i ** 2] += a[i]
print(a[100])