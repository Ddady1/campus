def mult_tuple(tuple1, tuple2):

    answer = []
    for n in tuple1:
        for d in tuple2:
            temp = (n, d)
            temp2 = (d, n)
            answer.append(temp)
            answer.append(temp2)

    return tuple(answer)




first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
print(mult_tuple(first_tuple, second_tuple))