def byfour (num):
    return num % 4 == 0

def four_dividers(number):

    return list(filter(byfour, range(1, number + 1)))










print(four_dividers(12))
print(four_dividers(3))