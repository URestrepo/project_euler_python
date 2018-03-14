"""
Lattice paths
Problem 15 
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20*20 grid?

This question can be solved using the binomial coefficient and using the number of up and down steps


(  a+b  )
    a


so using the equation we obtain

         (a+b)!
       _________
         (b)!*a!

"""

def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

def lattice_path(a,b):
    return fac(a+b)/(fac(b)*fac(a))

if __name__ == '__main__':
    print(lattice_path(20,20))