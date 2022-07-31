def combine_coins(cur, num):
    return ', '.join([(cur + str(i)) for i in num])




print(combine_coins('$', range(5)))
