def sequence_del(my_str):

    new_str = ''
    for n in my_str:
        if n in new_str and new_str.endswith(n):
            continue
        else:
            new_str += n
    return new_str

print(sequence_del("ppyyyyythhhhhooonnnnn"))