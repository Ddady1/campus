def count_chars(my_str):

    my_dict = {}
    for n in my_str:
        if n == ' ':
            pass
        else:
            f = my_str.count(n)
            my_dict[n] = f
    return my_dict




magic_str = "abra cadabra"
print(count_chars(magic_str))