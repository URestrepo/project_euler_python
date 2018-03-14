"""
Special Pythagorean triplet
Problem 9 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_triplets(sum):
    return [(a,b,c) for a in range(1,1000) for b in range(1,1000-a) for c in range(1,1000) if a**2+b**2 == c**2 and a+b+c == 1000]
    # return [(a,b,c) for a in range(1,20) for b in range(1,20-a) for c in range(1,20) if a**2+b**2 == c**2 and a+b+c == 30]

# if a+b+c == 1000 and 
# [(a,b) for a in range(1,20) for b in range(1,20-a)]

if __name__ == "__main__":
    product_triplet = find_triplets(sum)
    print product_triplet