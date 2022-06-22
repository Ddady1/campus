def seven_boom(end_number):
    new_list = []
    for n in range(end_number + 1):
        if (n % 7 == 0) or ('7' in str(n)):
            new_list.append('BOOM')
        else:
            new_list.append(n)

    return new_list







print(seven_boom(17))