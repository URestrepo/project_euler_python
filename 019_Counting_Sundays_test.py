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

# def count_sundays(start_year,end_year):
#     year = start_year
#     period = 1
#     sundays = list()
#     m = 0
#     d = ""
#     for year in range(start_year,end_year+1):
#         for month in range(1,12+1):
#             m = days_of_month(year,month)
#             if m == 29:
#                 sundays.append(year)
#             # for day in range(1,m):
#                 # d = day_name(period)
#                 # sundays.append((year,month,day))
            
#                 #period += days_of_month(year, month)
#             # if period % 7 == 0:
#             #     sundays.append((year,month))
#     return sundays


def count_sundays(start_year,end_year):
    year = start_year
    period = 1
    sundays = list()
    m = 0
    d = ""
    for year in range(start_year,end_year+1):
        for month in range(1,12+1):
            m = days_of_month(year,month)
            # if m == 29:
            sundays.append((year,month,m))
    return sundays


def day_name(num):
    if num % 7 == 1:
        return "Monday"
    if num % 7 == 2:
        return "Tuesday"
    if num % 7 == 3:
        return "Wednesday"
    if num % 7 == 4:
        return "Thursday"
    if num % 7 == 5:
        return "Friday"
    if num % 7 == 6:
        return "Saturday"
    if num % 7 == 0:
        return "Sunday"

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
    if month == 2:
        if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
            return 29
        else:
            return 28

if __name__ == "__main__":
    sundays = count_sundays(1900,2000)
    print(sundays)
    # num_sundays = len(sundays)
    # print("The number of 1st month Sundays in the years 1900 and including 2000 is " + str(num_sundays))









