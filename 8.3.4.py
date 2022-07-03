def inverse_dict(my_dict):

    new_dict = {}
    lst = []
    l_lst = []
    for k, v in my_dict.items():
        lst = [v, k]
        l_lst.append(lst)

    temp = l_lst[0]

    for n in range(1, len(l_lst) -1):
        if l_lst[n][0] == temp[0]:
            temp.append(l_lst[n][1])
            l_lst.remove(l_lst[n])

    for f in l_lst:
        for t in range(len(f) - 1):
            new_dict.update({f[0]: f[t + 1]}) #f[0]] = f[t + 1]


    print(l_lst)
    return new_dict




course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))