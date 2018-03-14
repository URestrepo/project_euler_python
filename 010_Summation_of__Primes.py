"""
Summation of primes
Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
from math_library import e_sieve


if __name__ = "__main__":
    primes = list(e_sieve(2000000))
    print sum(primes)