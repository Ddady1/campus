def arrow(my_char, max_length):

    new_str = ''
    for n in range(1, max_length + 1):
        new_str += (my_char * n)
        if n == max_length:
            break
        new_str += ('\n')
        n += 1

    while max_length > 0:
        if max_length == 1:
            break
        new_str += ('\n' + my_char * (max_length -1))
        max_length -= 1
    return new_str

x = (arrow('*', 5))
print(x)

