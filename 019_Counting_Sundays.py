"""
Counting Sundays
Problem 19 
You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
  A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

"""

for i in range 1900 and 2001:
    if year % 4 == 0 and year % 

    if month == 0,:
        return 31
    if month == 0:
        return 31
    if month == 0:
        return 31


"""

def count_sundays(start_year,end_year):
    year = start_year
    period = 1
    sundays = list()
    for year in range(start_year,end_year+1):
        for month in range(1,12+1):
            if period % 7 == 0:
                sundays.append((year,month))
            period += days_of_month(year, month)
    return sundays





def days_of_month(year,month):
    """

    """
    if month == 1:
        return 31
    elif month == 2:
        if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
            return 29
        else:
            return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31

def test_f(year,month):
    """
    Num year -> Num month -> num (28 or 29)
    This function simply checks for a given year with the assumption that the month is 2
    if the 
    """
    if month == 2:
        if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
            return 29
        else:
            return 28

def filter_years(start_year, xss):
    years_to_eliminate = 1900-start_year
    filter(lambda item: item[0] != year for year in irange(1900,start_year), xss)
    # filter(lambda item: item[0] != year for year in irange(1900,start_year), xss)


if __name__ == "__main__":
    sundays = count_sundays(1900,2000)...
    sundays_no_1900 = filter(lambda item: item[0] != year for year in range(1900,1901), sundays)
    num_sundays = len(sundays_no_1900)
    print("The number of 1st month Sundays in the years 1901 and including 2000 is " + str(num_sundays))









