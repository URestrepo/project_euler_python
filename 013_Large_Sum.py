"""
Using Problem 13 Data
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

from math_library import concat, product
from io_library import read_data


if __name__ == "__main__":
    data = read_data('Problem_13_data.txt')
    strings = concat(data)
    nums = map(int, strings)
    sum_ints = reduce(lambda x,y: x+y, nums)
    str_num = str(sum_ints)
    print str_num[0:10]