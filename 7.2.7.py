def arrow(my_char, max_length):

    #new_str = '1'
    for n in range(max_length):
        new_str += (my_char * n)
        new_str += ('\n')
        n += 1
    while max_length > 0:
        new_str += (my_char * max_length + '\n')
        max_length -= 1
    return new_str

x = (arrow('*', 5))
print(x)

