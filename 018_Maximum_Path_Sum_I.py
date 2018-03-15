"""
Maximum path sum I
Problem 18 
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                  75
                 95 64
                17 47 82
               18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
         41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
       53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
     91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

"""
from io_library import read_data
from math_library import concat

def reduce_max(lst1,lst2):
        # if len(lst1) != len(lst2)-1:
            # print("One of the lists is too long. Try switching")
        # else:
        if len(lst1) == 1:
            return lst1[0]
        else:
            print([max(lst2[i]+lst1[i],lst2[i]+lst1[i+1]) for i, item in enumerate(lst2)])
            return [max(lst2[i]+lst1[i],lst2[i]+lst1[i+1]) for i, item in enumerate(lst2)]


def reduce_max2(lst1,lst2):
        # if len(lst1) != len(lst2)-1:
            # print("One of the lists is too long. Try switching")
        # else:
        # if len(lst1) == 1:
            # return lst1[0]
        # else:
            # print ([lst1[i]+lst2[i] if lst1[i]+lst2[i] > lst1[i]+lst2[i+1] else lst1[i]+lst2[i+1] for i, item in enumerate(lst1)])
            # return [lst1[i]+lst2[i] if lst1[i]+lst2[i] > lst1[i]+lst2[i+1] else lst1[i]+lst2[i+1] for i, item in enumerate(lst1)]
            print (max(lst1[i]+lst2[i], lst1[i]+lst2[i+1]) for i, item in enumerate(lst1)])
            return [lst1[i]+lst2[i] if lst1[i]+lst2[i] > lst1[i]+lst2[i+1] else lst1[i]+lst2[i+1] for i, item in enumerate(lst1)]


def intify(xss):
    for item in xss:
        splitify = item.split()
        for num in splitify:
            int(num)
            

if __name__ = "__main__":
    data = read_data("Problem_18_data.txt")
    # data_split = map(lambda x: map(x.split), data)
    data_split = [concat([strings.split() for strings in row]) for row in data]
    # data_split = map(lambda row: map(lambda x: x.split(), x), data) not working
    triangle_nums = map(lambda d: map(int,d),data_split)
    reduced_triangle = reduce(reduce_max, reversed(triangle_nums))
    reduced_triangle2 = reduce(reduce_max2, triangle_nums)


