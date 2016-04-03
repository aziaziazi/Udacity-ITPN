# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

def draw_shape(t,d,p):
	#if cicle
	if p==0:
		t.up()
		t.right(90)
		t.forward(d)
		t.right(270)
		t.down()
		t.circle(d)
		t.up()
		t.right(270)
		t.forward(d)
		t.right(90)
		t.down()
	#if not circle
	elif p!=0:
		for i in range (0,p):
			t.forward(d)
			t.right(360/p)
			i +=1

	# t= turtle
	# d = distance/rayon
	# p = pattern : 0> circle 2>line 3>triangle 4>square 6>hexagon...
	# r = rotations
	# c = color
def turtx(t,d,p,r,c):
	t = turtle.Turtle()
	t.shape("turtle")
	t.speed(0)
	t.tracer(10,0)
	t.color(c)
	for i in range (0,r):
		draw_shape(t,d,p)
		t.right(360/r)

def draw_path():
	window = turtle.Screen()
	window.bgcolor("black")

	# turtx(turtle,distance,pattern,rotation,color)
	# p=0 > circle
	turtx("brad",300,0,1,"white")
	# p=4 > square
	turtx("brad",30,4,22,"grey")
	# p=2 > lines
	turtx("brad",60,2,13,"blue")
	turtx("brad",80,2,9,"green")
	turtx("brad",150,2,7,"yellow")
	turtx("brad",300,2,5,"orange")
	# hexagon
	turtx("brad",60,6,7,"red")
	window.exitonclick()

draw_path()


