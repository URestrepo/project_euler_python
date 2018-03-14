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