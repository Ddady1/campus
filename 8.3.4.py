def inverse_dict(my_dict):

    new_dict = {}
    lst = []
    l_lst = []
    for k, v in my_dict.items():
        lst = [k, v]
        l_lst.append(lst)

    for n in l_lst:
        for f in n:
            if n[1] in my_dict:
                n.append(n[0])
            new_dict.update(n)
    print(new_dict)

    print(l_lst)
    return new_dict




course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))