import urllib

def readText(filePath):
	text = open(filePath)
	content_of_text = text.read()
	# print "text to check : %s" %content_of_text
	text.close()

	response = WDYL(content_of_text)
	if "true" in response:
		print "Give a shit a it before sending ;)"
	elif "false" in response:
		print "Clear !"

def WDYL(text):
	connexion = urllib.urlopen("http://www.wdyl.com/profanity?q=%s" %text)
	output = connexion.read()
	print "output = %s" % output
	return output
	connexion.close()

readText("./3.3 Movies quotes.txt")