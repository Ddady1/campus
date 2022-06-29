def func(s):

    return float(s[1])

def sort_prices(list_of_tuples):

    x = (sorted(list_of_tuples, key=func))
    x.reverse()
    return x





products = [('milk', '5.5'), ('bread', '5.51'), ('candy', '2.50'), ('bread', '9.0')]
print(sort_prices(products))