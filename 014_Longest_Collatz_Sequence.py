"""
Longest Collatz sequence
Problem 14 
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from math_library import odd, even
from operator import itemgetter

def collatz_sequence(num):
    """
    Num a -> [Num a]
    This function creates a list of the numbers that come appear in a Collatz Sequence.

    """
    sequence = list()
    sequence.append(num)
    while num != 1:
        num = equation_decision(num)
        sequence.append(num)
    return sequence



def equation_decision(n):
    if even(n):
        return n/2
    else:
        return (3*n+1)

def longest_sequence(num_range):
    sequences = [collatz_sequence(num) for num in range(1,num_range)]
    num_and_sequence_len = [(s[0],len(s)) for i, s in enumerate(sequences)]
    sorted_num_sequence_len = sorted(num_and_sequence_len, key=itemgetter(1), reverse=True)
    return sorted_num_sequence_len[0]


if __name__ == "main":
    # sequences = [collatz_sequence(num) for num in range(1,100)]
    print(longest_sequence(1000000))


