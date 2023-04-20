def f(s, e):
    if s == e:
        return 1
    # если мы перепрыгнули конец или попали в цифру которую надо обойти
    if s > e or s == 5:
        return 0
    return f(s + 1, e) + f(s * 2, e)


print(f(1, 10) * f(10, 20))