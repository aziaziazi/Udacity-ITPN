import time
import webbrowser


def sleeper():
		num = raw_input("How long do I set up your timer ?")
		num = float(num)

		occurency = raw_input("How many times ?")
		occurency = int(occurency)


		print ("Timer Start at " + time.ctime())

		for c in range (0,occurency) :
			print "occurency number {c} will start in {occurency} seconds !".format(c=c, occurency=occurency)
			time.sleep(num)
			webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

sleeper()