# -----------
# User Instructions
#
# Modify the valid_month() function to verify
# whether the data a user enters is a valid
# month. If the passed in parameter 'month'
# is not a valid month, return None.
# If 'month' is a valid month, then return
# the name of the month with the first letter
# capitalized.
#

## MY METHOD
## Works
# months = {'January':1,
#           'February':1,
#           'March':1,
#           'April':1,
#           'May':1,
#           'June':1,
#           'July':1,
#           'August':1,
#           'September':1,
#           'October':1,
#           'November':1,
#           'December':1}


# def valid_month(month):
#      month = month.capitalize()
#      if month in months :
#           return month
#      else :
#           return None

## UDACITY

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_dic = dict((m[:3].lower(),m) for m in months)
# print month_dic

def valid_month(month):
     if month:
          short_month = month[:3].lower()
          # print "short_month = " + short_month

          # Are those the same ?
          # print "month_dic[] = "+ month_dic[short_month]
          # print "month_dic.get() = "+ month_dic.get(short_month

          return month_dic.get(short_month)



print valid_month("ezopuzhttp://thenextweb.com/dd/2014/11/24/differently-learning-code-today/")
print valid_month("jAnuaRY")
print valid_month("jan093?KNE")
# print valid_month("jaanuary") # 3 first letters has to be good


