import webbrowser
import time


total_breaks = 2
break_count = 0

print "This programm started on " + time.ctime()
while break_count<total_breaks:
	time.sleep(1)
	webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
	break_count +=1
