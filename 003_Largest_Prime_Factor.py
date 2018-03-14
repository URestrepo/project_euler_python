"""
Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#Function is_prime
#checks to see if number is prime



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

if __name__ == "__main__":
    print max(prime_factorize(600851475143))
