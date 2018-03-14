"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math_library import e_sieve, nth_prime_estimator

def nth_prime(n):
    primes = list(e_sieve(int(nth_prime_estimator(n))))
    return primes[n-1]

if __name__ == "__main__":
    print nth_prime(10001)
