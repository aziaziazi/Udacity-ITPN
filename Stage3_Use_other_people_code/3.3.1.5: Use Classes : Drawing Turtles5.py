# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

def draw_turn(brad,d,p):
	brad.forward(d)
	brad.left(360/p)

def draw_shape(brad,i,d,p):

	if i==0:
		for m in range (0,p):
			draw_turn(brad,d/2,p)
		draw_turn(brad,d,p)

	else:
		for m in range (0,p):
			draw_shape(brad,i-1,d/2,p)
		draw_turn(brad,d,p)

def turtx(i,d,p):

	# Init
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("orange")
	# Console
	dis = d/(2**i)
	print """
	edges = {p}
	iteration = {i}
	total size = {d}
	element size = {dis}""".format(i=i, d=d, p=p, dis=dis)

	# Draw acceleration
	brad.speed(0)
	brad.tracer(100,0)

	draw_shape(brad,i,d,p)

def draw_path(i,d,p):
	window = turtle.Screen()
	window.bgcolor("black")
#	turtx(iteration (i), total size(d), edges(p))
	turtx(i,d,p)
	window.exitonclick()

# iteration (i), total size(d), edges(p)
draw_path(4,300,5)


