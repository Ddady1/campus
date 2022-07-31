def combine_coins(coin, numbers):
    output = ""
    for num in numbers:
        output += coin + str(num) + ', '
     # Ignore the last comma.
    return output[:-2]


print(combine_coins('$', range(5)))
