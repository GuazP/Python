def wynik(items_):
    return items_ + [sum(items_)]

def transformacja(items_):
    return [i/items_[0] for i in items_]

def nowy_X(items_):
    return items_[-1]

def przemnoz_rownanie(items_, nowy_x):
    return [items_[-1]] + [i*nowy_x for i in items_[2:3]]

def rownanie(items_, round_):
    items_ = wynik(items_)
    print(items_)
    items_ = transformacja(items_)
    print(items_)
    nowy_x = nowy_X(items_)
    print(nowy_x)
    items = przemnoz_rownanie(items_, nowy_x)
    print(items_)
    while True:
        items_ = wynik(items_)
        print(items_)
        break

rownanie([2, -0.4, 0.3], 3)
