"""
Smallest multiple
Problem 5 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

This is an interesting problem because it can be solved using mathematical properties rather than by brute forcing.
there may be a way to use yield though I will look at that later

The smallest number divisible by all numbers in a range must be divisible by all prime numbers in a range
so given a list of a range, check to see if numbers in the range divide other numbers in the list. If so, divide that number by one
of the divisor

"""

from math_library import e_sieve
import math

def divisable_by_all_range(n):
    """

    """
    primes = list(e_sieve(n))
    largest_powers = map(lambda x: get_largest_power(n,x),primes)
    nums = [primes[i]**largest_powers[i] for i,item in enumerate(primes)]
    # nums = map(lambda t : primes[t[0]]**largest_powers[t[0]], enumerate(primes))
    return reduce(lambda x,y: x*y, nums)


def get_primes_up_to_n(n):
    return list(e_sieve(n))

def get_largest_power(n,x):
    """
    Find the highest integer power of x that does not exceed n.
    > get_largest_power(10,2)
    3
    """
    return int(math.log(n)/math.log(x))


if __name__ == "__main__":
    print divisable_by_all_range(20)