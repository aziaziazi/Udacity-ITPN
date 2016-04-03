import urllib

def read_text():
	quotes = open("./3.3 Movies quotes.txt")
	contents_of_files = quotes.read()
	print contents_of_files
	quotes.close()

	check_profanity(contents_of_files)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    if 'true' in output:
    	print "Profanity alert !"
    elif "false" in output:
    	print "Nice document"
    else:
    	"Can't check :("
    connection.close


read_text()