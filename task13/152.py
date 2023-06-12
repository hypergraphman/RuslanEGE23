g = {
    'А': 'БГ',
    'Б': 'Д',
    'В': 'АБГДЖ',
    'Г': 'Ж',
    'Д': 'ЗКЕ',
    'Е': 'ВКИ',
    'К': 'ЕИ',
    'И': 'ЕЖ',
    'Ж': 'Е',
    'З': 'К',
}


def f(v, p):
    if len(p) > 1 and p[0] == p[-1]:
        return 1
    if len(p) > len(set(p)):
        return 0
    s = 0
    for i in g[v]:
        s += f(i, p + i)
    return s


print(f('Е', 'Е'))