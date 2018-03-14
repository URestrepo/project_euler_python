"""
Factorial digit sum
Problem 20 
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

if __name__ == '__main__':
    product = fac(100)
    str_product = str(product)
    nums = map(int, str_product)
    sum_nums = sum(nums)