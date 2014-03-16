def dividers(x):
    return [i for i in range(1, x) if x % i == 0]

print(dividers(10))


def to_bool(lst):
    return [bool(el) for el in lst]

print(to_bool([0,1,'','a',None,]))