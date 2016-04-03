# Lession 4.7: Introducing Templates

# We introduce templates to build complicated strings using the Jinja2 library.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4186408748/m-686598825

import os

import jinja2
import webapp2

# Set up jinja environment
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


class Handler(webapp2.RequestHandler):

### USE FOR BASIC TEMPLATES
### Why render and render_str doenst loop forever ?
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render (self, template, **kw):
        self.write(self.render_str(template, **kw))
###


class MainPage(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", items = items)

# class fizzbuzz(Handler):
#     def get(self):
#         n = self.request.get("n")
#         n = n and int(n)
#         self.render("fizzbuzz.html", n=n)


app = webapp2.WSGIApplication([("/", MainPage),
                                # ("/fizzbuzz", fizzbuzz)
                                ],
                                debug=True)
