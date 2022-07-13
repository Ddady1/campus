import functools
def f(a, b):
    if a < b:
        return a
    else:
        return b


l = [47,11,42,102,13]
print(functools.reduce(f, l ,10))