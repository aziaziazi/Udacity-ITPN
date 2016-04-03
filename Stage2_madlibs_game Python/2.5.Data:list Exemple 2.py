# Lesson 2.6: For Loops

# For loops, like while loops, are useful for running a block of code
# multiple times. For loops make iterating through elements in a list
# easier than using a while loop.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4152219158/m-48204891

def print_all_elements(p):
    for e in p:
        print e

myList = [1, 2, [3, 4]]
print_all_elements(myList)

# Add your own code and notes here







# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.


def sum_list(inputs):
    total = 0
    for element in inputs:
        total += element

    return total


print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134








# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.

def measure_udacity(test_list):
    total = 0
    for e in test_list:
        if e[0] == "U":
            total +=1
    return total



print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2









# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(liste,to_find):
    count = 0

    for e in liste:
        if e == to_find:
            return count
        count +=1
    return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1






# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.


def find_element(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1

    index = p.index(t)



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1