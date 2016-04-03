# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle




def draw_edge(brad,dis,i):
	if i==0:
		brad.forward(dis)
	else:
 		draw_edge(brad,dis, i-1)
 		brad.left(60)
 		draw_edge(brad,dis, i-1)
		brad.right(120)
 		draw_edge(brad,dis, i-1)
 		brad.left(60)
 		draw_edge(brad,dis, i-1)

def draw_shape(brad,i,d,p):
	dis = d/(i*i)

	print """
	i = {i}
	d = {d}
	p = {p}
	dis = d/i = {dis}""".format(i=i, d=d, p=p, dis=dis)

	for m in range (0,p):
		draw_edge(brad, dis,i)
		brad.right(360/p)

	# i = etapes
	# d = distance/rayon
	# p = pattern : 0> circle 2>line 3>triangle 4>square 6>hexagon...

def turtx(i,d,p,c):


	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.speed(0)
	brad.tracer(48,0)
	brad.color(c)
	draw_shape(brad,i,d,p)

	angie = turtle.Turtle()
	angie.shape("turtle")
	angie.speed(0)
	angie.color("blue")
	angie.forward(d)

def draw_path():
	window = turtle.Screen()
	window.bgcolor("black")

	# turtx(etapes,distance,pattern,color)
	# p=3 > triangle
	turtx(6,300,3,"orange")

	window.exitonclick()

draw_path()


