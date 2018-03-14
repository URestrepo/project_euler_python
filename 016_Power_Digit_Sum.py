"""
Power digit sum
Problem 16 
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


if __name__ = "__main__":
    num = 2**1000
    str_num = str(num)
    sum_digits = reduce(lambda x,y: x+y, map(int, str_num))
    print(sum_digits)