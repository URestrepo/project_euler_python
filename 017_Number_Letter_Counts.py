"""
Number letter counts
Problem 17 
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
from math_library import concat


ones = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]



def number_to_word(num):
    """
    Num -> String
    
    Function converts a number into the word representation of that number. Function
    only goes up to 1000
    """
    """
    Num a -> [Num a]
    This function creates a list of the numbers that come appear in a Collatz Sequence.
    """
    if num == 0:
        return ''
    elif num >= 1 and num < 20:
        return ones[num]
    elif num >= 20 and num < 100:
        return tens[num/10] + ones[num % 10]
    elif num >= 100 and num % 100 == 0 and num < 1000:
        return ones[num/100] + "hundred"
    elif num >= 100 and num <= 999:
        return ones[num/100] + "hundredand" + number_to_word(num % 100)
    # elif num >= 100 and num < 999 and num % 100 < 20:
    #     return ones[num/100] + number_to_word(num % 100)
    # elif num >= 100 and num < 999 and num % 100 > 20:
    #     return ones[num/100] + number_to_word(num % 100)
    else:
        return "onethousand"


def add_word_numbers(num):
    num_string = concat([number_to_word(i) for i in xrange(num+1)])
    return concat([number_to_word(i) for i in xrange(num+1)])

if __name__ == "__main__":
    number_string = add_word_numbers(1000)
    print(len(number_string))