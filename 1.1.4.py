import functools

def sumall(mis1, mis2):

    return int(mis1) + int(mis2)

def sum_of_digits(number):

    return functools.reduce(sumall, str(number))




print(sum_of_digits(104))
