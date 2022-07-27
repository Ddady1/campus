def is_prime(number):


    return 0 not in [number % x for x in range(2, number//2+1)]
    #return [False if number % x == 0 else True for x in range(2, number)]
    #return result










print(is_prime(11))
print(is_prime(21))
