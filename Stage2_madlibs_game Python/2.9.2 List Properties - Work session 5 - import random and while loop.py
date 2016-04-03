# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data

# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.

# To create a random integer from 0 to 10, we first import the
# "random" module

import random

# We then print a random integer using the random.randint(start, end) function
print "Random number generated: " + str(random.randint(0,10))

# Remember that if we want to concatenate a string and a number, we need to convert the
# integer into a string using the str() function

# We now want to create a list filled with random numbers. The list should be
# of length 20

list4 = []
list_length = 20

# Write code here and use a while loop to populate this list of random integers. A crucial
# function that will help you is to use the append() method to add elements to a list.

# I created a function for separating the task
# Its not necessary, the course doesnt create the function
def random_list(list_to_populate, length):
	while len(list_to_populate) < length:
		list_to_populate.append(random.randint(0,10))

random_list(list4,list_length)
# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
print list4