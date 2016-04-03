# Lesson 3.4: Make Classes
# Mini-Project: Draw Turtles

# Sometimes we want to define classes that may have similarities.
# For example, a TVShow class and a Movie class would both have a title attribute.
# To cut down on repitition we can have classes inherit from each other.
# So in our example we could have both TVShow and Movie inherit from a class
# Video which includes all the shared attributes between Movie and TVShow.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4195428894/m-1016138543


class Parent(object):
	def __init__(self, last_name, eye_color):
		print "Parent Constructor Called !"
		self.last_name = last_name
		self.eye_color = eye_color

	def printname(self):
		last_name = self.last_name
		print "parent last_name : " + str(last_name)

# papa_gab = Parent("Gabrieli", "Brown")
# print papa_gab.last_name

class Child(Parent):
	print "Child Called !"
	def __init__(self, last_name, eye_color, number_of_toys):
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

	def printname(self):
		last_name = self.last_name
		print "child last_name : " + str(last_name)


cam_gab = Child("Gabrieli", "Brown", "A lot !")

cam_gab.printname()


