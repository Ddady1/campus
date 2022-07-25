def is_prime(number):

    result = [False if x % 2 == 0 else True for x in range(2, number)]
    return result










print(is_prime(42))
print(is_prime(43))
