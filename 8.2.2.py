def sort_prices(list_of_tuples):
    sorted_lst = []
    flag = len(list_of_tuples)
    #sorted_lst = list_of_tuples.sort()
    for n in list_of_tuples:
        num = float(n[1])
        if sorted_lst == []:
            sorted_lst.append(n)
            temp = num
        else:
            if num <= temp:
                sorted_lst.append(n)

            else:




        #print(type(num))
        #print(num)
    print(sorted_lst)
    print(type(sorted_lst[0][0]))
    print(sorted_lst.sort())



products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)