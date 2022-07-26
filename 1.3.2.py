def is_prime(number):

    result = [False if number % x == 0 else True for x in range(2, number)]
    return result










print(is_prime(25))
print(is_prime(24))
