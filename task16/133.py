from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return (3 * n + 5) * f(n - 1)


for i in range(2100):
    f(i)

print(f(2073) / f(2070))

