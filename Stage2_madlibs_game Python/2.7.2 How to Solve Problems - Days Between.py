# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def is_equal(year1, month1, day1, year2, month2, day2):

    # return (year1==year2 and month1 == month2 and day1 == day2);

    if year1==year2:
            if month1 == month2:
                if day1 == day2:
                    return True



    else:
        return False



def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    ''' count = 0
    if year1 == year2:
        if month1 == month2:
            if day1 == day2:
                return True

    while year1 != year2 or month1 != month2 or day1 != day2:
        if day1 < 30:
            day1 += 1
            count +=1
        else:
            if month1 == 12:
                year1 += 1
                month1 = 1
                day1 = 1
                count +=1
            else:
                month1 += 1
                day1 = 1
                count +=1
    return count'''

    '''count=0

    while count<5:
        print count
        if day1 < 30:
            day1 += 1
        else:
            if month1 == 12:
                year1 += 1
                month1 = 1
                day1 = 1
            else:
                month1 += 1
                day1 = 1'''
    count = 0
    while not is_equal(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        count +=1
    return count




  #  while is_equal(year1, month1, day1, year2, month2, day2) == False:
   #     nextDay(year1,month1,day1)

   #     print year1 + month1 + day1
   # print year1, month1, day1

    # YOUR CODE HERE!


print daysBetweenDates(2012,9,30,2012,10,30)

'''def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"
'''
print daysBetweenDates(2015,10,30,2015,12,24)

