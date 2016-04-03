# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48727556/m-48724313

print 2 < 3
print 21 < 3
print 7 * 3 < 21
print 7 * 3 != 21
print 7 * 3 == 21

# Add your own code and notes here



print "Example 1: Greater-than and less-than comparisons"
print 2 > 1
print 1 > 2
print 5 < 20
print 100 < 19


print "Example 2: Equality and non-equality comparisons"
print 5 == 5
print "hello" == "hello"
print 5 == 10
print 5 == '5' # what do you think will happen here?
print 7 != 10
print 7 != 7


print "Example 3: A demo of what you are about to learn"
if 3 < 5:
    print "Three is definitely smaller than 5!"

if 10 > 20:
    print "Did you know that 10 is greater than 20!?"
else:
    print "20 is greater than 10"




# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'


def is_friend(name):
    if name[0] == "D":
        return True
    else:
        return name[0] == "N"


print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False

#True and false
print True or False 	# True
print True or True 		# True
print False or True		# True
print False or False 	# False

#print xxx				# Error
#print xxx or True		# Error
#print xxx or False 	# Error
print True or xxx		# True
#print False or xxx		# Error

print "xxx"				# xxx
print "xxx" or True		# xxx
print "xxx" or False 	# xxx
print True or "xxx"		# True
print False or "xxx"	# xxx

#If the 1st value is TRUE, then return True
#If the 1st value is FALSE, then return 2nd Value




# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

#my solution :
def biggest(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
    if n2>n3:
        return n2
    else:
        return n3

#Dave's solution
def dave_biggest(n1,n2,n3):
	if n1>n2:
		if n1>n3:
			return n1
		else:
			return n3
	else:
		if n2>n3:
			return n2
		else:
			return n3


print dave_biggest(3, 6, 9)
#>>> 9

print dave_biggest(6, 9, 3)
#>>> 9

print dave_biggest(9, 3, 6)
#>>> 9

print dave_biggest(3, 3, 9)
#>>> 9

print dave_biggest(9, 3, 9)
#>>> 9
