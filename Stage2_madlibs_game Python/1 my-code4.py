# Lesson 2.3: Procedures

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4141089439/m-48667860

def rest_of_string(s):
    return s[1:]

print rest_of_string('audacity')

# Add your own code and notes here







def say_hello(name):
    greeting = "Hello " + name + '!'
    return greeting

print say_hello("Camille")
# In the previous example, you saw code that looked like what you see above.
# Look at the first line. In that line, 'name' is a "parameter"
# of the function say_hello

# In the code below, the add_two_numbers function has two parameters.
# What do you think will happen when you press "Test Run"?
# Make a prediction and then press "Test Run"
def add_two_numbers(number_1, number_2):
    return number_1 + number_2

print add_two_numbers(4, 3)
print add_two_numbers(2, 6)
print add_two_numbers(0, 9)

# Once you've pressed Test Run, remove the comment characters from the
# code below and then make ONE modification so that the function does
# what the name says it should do.

def subtract_two_numbers(number_1, number_2):
    return number_1 - number_2

print subtract_two_numbers(4, 3)


def sum(a,b):
	a=a+b
#that does nothing ! Because no return


def sum(a,b):
	a=a+b
	return a

print sum(2,88)
#that works !


def sum(a,b):
	a=a+b
	return a
a = 2
b = 88
print sum(a,b)
print a
# the function does it jobs and return a+b
# But the value a remains the same outside of the function.