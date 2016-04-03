# Lession 4.5: Hello Webapp World
#
# This starter code will illustrate how we can create a webserver that writes out
# a "Hello World" to the browser usig the webapp2 library.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4150259168/m-48722218

import webapp2

# form method="post" => (default : "get") Ok but change testhandler
form="""
<form method="post" action="/testform">
<input name="q">
<input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
	def get(self):
		# Content type header => commented because default is "text/html"
		# self.response.headers["Content-Type"] = "text/plain"

		# self.response => object represent the response
		# we send back to the client
		self.response.out.write(form)

class TestHandler(webapp2.RequestHandler):
	def post(self):
		# self.request => represent the request that came from the browser
		# .get => get a specific paramater
		q = self.request.get("q")
		self.response.out.write(q)

	  # Test line > print http request
		# self.response.headers["Content-Type"] = "text/plain"
		# self.response.out.write(self.request)

app = webapp2.WSGIApplication([("/", MainPage),
															# Add a parenthesis for each
																("/testform", TestHandler)],
																debug = True)
