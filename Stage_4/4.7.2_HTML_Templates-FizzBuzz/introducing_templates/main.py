# Lession 4.7: Introducing Templates

# We introduce templates to build complicated strings using the Jinja2 library.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4186408748/m-686598825

import os

import jinja2
import webapp2

# Set up jinja environment

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

# Instructor Notes:
# Suggest to print out template_dir to see how the file path is being constructured.
# You can find the print out in the Logs in Google App Engine (GAE). For Windows and Mac users,
# you need to click on the "Logs" button to be able to see the print messages

print "template_dir is here >>> " + template_dir

class Handler(webapp2.RequestHandler):
### USE FOR BASIC TEMPLATES
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render_html (self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        n = self.request.get("n")
        self.render_html("shopping_list.html", n=n)

class fizzbuzz(Handler):
    def get(self):
        n = self.request.get("n")
        n = n and int(n)
        self.render_html("fizzbuzz.html", n=n)


app = webapp2.WSGIApplication([("/", MainPage),
                                ("/fizzbuzz", fizzbuzz)],
                                debug=True)
