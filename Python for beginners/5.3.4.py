def last_early(my_str):
    my_str = my_str.lower()
    if my_str.count(my_str[-1::]) > 1:
        return True
    else:
        return False