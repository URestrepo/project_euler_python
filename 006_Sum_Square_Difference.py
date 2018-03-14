"""
Sum square difference
Problem 6 
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def sum_squares(n):
    return ((n*(n+1)*(2*n+1))/6)

def square_sum(n):
    return (n*(n+1)/2)**2

def diff_square_sum_and_sum_squares(n):
    return square_sum(n)-sum_squares(n)

def diff_square_sum_and_sum_squares2(n):
    return ((n*(n+1))*(3*(n*n)-n-2))/12

if __name__ == "__main__":
   print diff_square_sum_and_sum_squares2(100)