def sort_prices(list_of_tuples):
    sorted_lst = list_of_tuples.sort(reverse=True, key=[1])
    '''for n in list_of_tuples:
        n[1] = float(n[1])
        print(type(n[1]))'''
    print(sorted_lst)



products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)