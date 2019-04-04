import itertools


def primes():
    a = 1
    while True:
        a += 1
        if all(a % i for i in range(2, a)):
            yield a


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]