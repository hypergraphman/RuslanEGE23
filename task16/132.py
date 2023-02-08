from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return (2 * n - 1) * f(n - 1)


for i in range(3550):
    f(i)

print(f(3516) / f(3513))
