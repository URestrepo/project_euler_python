"""
Largest palindrome product
Problem 4 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def check_palindrome(word):
    if len(word) < 2:
        return True
    elif word[0] == word[-1]:
        return True and check_palindrome(word[1:-1])
    else:
        return False

def find_largest_3_digit_palindromes():
    palindromes_multiples = sorted(filter(check_palindrome, set(str(a*b) for a in range(100,1000) for b in range(100,1000))))
    return max(map(lambda x: int(x),palindromes_multiples))


print(find_largest_3_digit_palindromes())