def concat(xss):
    return reduce(lambda x,y: x+y, xss)

def hundred_years():
    return ([1,0,0,0]*25 + [0])[1:]

def week_pattern():
    return concat([[(2,),(3,),(4,),(5,),(6,),(7,),(1,)] for i in xrange((52*101))])

def convert_bin_to_days(n):
    if n == 1:
        return 366
    elif n == 0:
        return 365
    else:
        return False

def convert_bin_to_months_and_days(b):
    return [(x,y) for x in xrange(1,13) for y in xrange(1, convert_months_to_days(x,b)+1)]

def convert_months_to_days(n,b):
    if n == 1: return 31
    elif n == 2 and b == 1: return 29
    elif n == 2 and b == 0: return 28
    elif n == 3: return 31
    elif n == 4: return 30
    elif n == 5: return 31
    elif n == 6: return 30
    elif n == 7: return 31
    elif n == 8: return 31
    elif n == 9: return 30
    elif n == 10: return 31
    elif n == 11: return 30
    elif n == 12: return 31
    else: return False

def calendar():
    return map(convert_bin_to_months_and_days, hundred_years())

def monday_check(xs):
    if xs[0] == 7 and xs[-1] == 1:
        return True
    else:
        return False

c = concat(calendar())
w = week_pattern()
calendar_with_days = map(concat, zip(w,c))
print calendar_with_days
# print len(filter(monday_check, calendar_with_days))