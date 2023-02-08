from functools import lru_cache


@lru_cache(None)
def f(x):
    if x <= 2:
        return 1
    elif x > 2:
        return f(x - 1) + f(x - 2)


for i in range(2000):
    f(i)

print(f(1450))