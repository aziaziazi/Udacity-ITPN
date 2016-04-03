# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):

   	if year%4!=0:
   		return "common"
   	elif year%100!=0:
   		return "leap"
   	elif year%400!=0:
   		return "common"
   	else:
   		return "leap"

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
	days = 0
	count = y1

	#days += 365*(y2-y1)

	while count<y2:
		print count
		if isLeapYear(count)=="common":
			days += 365
		else:
			days += 366
			print "LEAP !"
		print "days : " + str(days)
		count+=1

	dif = days_from_0(m2,d2) - days_from_0(m1,d1)
	days += dif
	return days


def days_from_0(m,d):
	days = 0
	count = 0
	while count < m:
		days += daysOfMonths[count]
		count += 1
	days += d
	return days


b_date = [2,6,1988]
c_date = [27,10,2015]


print daysBetweenDates(b_date[2],b_date[1],b_date[0],c_date[2],c_date[1],c_date[0])

# >>> Show 10010 instead of 10008 :(
