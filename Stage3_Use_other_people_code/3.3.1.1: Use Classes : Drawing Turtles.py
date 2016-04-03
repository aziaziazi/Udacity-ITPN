# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

# # Your code here.$

# t= turtle
# d = distance
# a = angles : 3>triangle 4>square 6>hexagon...
def draw_shape(t,d,a):
	for i in range (0,a):
		t.forward(d)
		t.right(360/a)
		i +=1

def hexagon(t,d):
	i=0
	while i<6:
		t.forward(d)
		t.right(60)
		i +=1
		print i

def brad(t):
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("white")
	brad.speed(0)

	turns = 20
	count = 0
	while count<turns:
		draw_shape(brad,20,4)
		brad.right(360/20)
		count+=1

def angie():
	angie = turtle.Turtle()
	angie.shape("turtle")
	angie.color("grey")
	angie.speed(10)

	hexagon(angie,50)

def draw_path():
	window = turtle.Screen()
	window.bgcolor("black")

	brad(brad)
	angie()


	window.exitonclick()

draw_path()


