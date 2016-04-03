# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))


''' My first method

def median(a,b,c):
    if a>b:
        if a>c:
            if b>c:
                return b
            else:
                return c
        else:
            return a
    else:

        if b>c:
            return c
        else:
            return b
'''



''' My second method

def median(a,b,c):
    if bigger(a,b) == bigger(a,c):
        return bigger(b,c)
    elif bigger(a,b)>bigger(a,c):
        return bigger(a,c)
    else:
        return bigger(a,b)
'''

'''My third method
def median(a,b,c):
    if biggest(a,b,c) == a:
        return bigger(b,c)
    elif biggest(a,b,c) == b:
        return bigger(a,c)
    else:
        return bigger(a,b)
'''


# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

'''My fourth method
def median(a,b,c):
    if  bigger(a,b) <= c:
        return bigger(a,b)
    elif bigger(a,c) <= b:
        return bigger(a,c)
    elif bigger(b,c) <= a:
        return bigger(b,c)
'''



# Udacity method
def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger (b,c)
    elif big == b:
        return bigger (a,c)
    else:
        return bigger (a,b)


print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7

print(median(2,3,1))





