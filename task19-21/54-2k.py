start = 5
win = 83


def f(a, b, c, m):
    if a + b >= win:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a * 4, b, c + 1, m), f(a, b * 4, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for i in range(1, win - start):
    for x in range(1, 5):
        if f(start, i, 0, x):
            print(i, x)
            break