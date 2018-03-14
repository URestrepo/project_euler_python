import math

def prime_factorize(n):
    results = list()
    num = n
    x = 2
    while num != 1:
        if num % x == 0:
            results.append(x)
            num = num / x
        else:
            x += 1
    return results


def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def odd(x):
    return not even(x)


def e_sieve(n):
    multiples = set()
    k = 2
    while k <= n:
        if k not in multiples:
            yield k
            multiples.update(range(k*k, n+1, k))
        k += 1
 
def nth_prime_estimator(n):
    """
    Rosser, Barkley (1941). "Explicit bounds for some functions of prime numbers".
    """
    return n * (math.log(n * math.log(n)))

# def sieve(n):
#     """
#     Recursive implementation, runs out of stack.
#     """
#     primes_lst = list()
#     pos = 2
#     while pos <= n:
#         if check(pos, primes_lst):
#             primes_lst.append(pos)
#         pos += 1
#     return primes_lst

# def check(num, lst):
#     if len(lst) == 0:
#         return True
#     elif num % lst[0] != 0:
#         return True and check(num, lst[1:])
#     else:
#         return False

# def sieve_list(n):
#     primes_lst = list()
#     composite_set = set()
#     pos = 2
#     while pos <= n:
#         if pos not in composite_set:
#             primes_lst.append(pos)
#             composite_set.update(range(pos**2,n+1,pos))
#         pos += 1
#     return primes_lst



def get_largest_power(n,x):
    """
    Find the highest integer power of x that does not exceed n.
    > get_largest_power(10,2)
    3
    """
    return int(math.log(n)/math.log(x))

def gcd(a,b):
    # if a < b:
    #     return gcd(b,a)
    # else:
    #     if a == b:
    #         return a
    #     else: 
    #         return gcd(b,a-b)
    while b:
        a, b = b, a%b
    return a

def lcm(a,b):
    return a * b // gcd(a,b)


def concat(xss):
    return reduce(lambda x,y: x+y, xss)


def product(xs):
    return reduce(lambda x,y: x*y, xs)



























































