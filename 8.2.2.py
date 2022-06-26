def sort_prices(list_of_tuples):
    sorted_lst = []
    flag = len(list_of_tuples)
    #sorted_lst = list_of_tuples.sort()
    for n in list_of_tuples:
        num = float(n[1])
        if n[0] == 0:

            sorted_lst.append(n)
        else:
            if num > sorted_lst[1]:
                sorted_lst.append(n)
            #else:



        print(type(num))
        print(num)
    #print(sorted_lst)



products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)