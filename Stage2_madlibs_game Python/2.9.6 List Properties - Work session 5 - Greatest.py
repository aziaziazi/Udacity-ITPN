# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):

#For method
	greatest = 0
	for i in list_of_numbers:
		if i > greatest:
			greatest = i
	return greatest

#While method
'''
	index = 0
	while len(list_of_numbers)>index:
		if list_of_numbers[index] > greatest:
			greatest = list_of_numbers[index]
		index +=1
	return greatest
'''
print greatest([1,2,3])
#>>> 3
print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0