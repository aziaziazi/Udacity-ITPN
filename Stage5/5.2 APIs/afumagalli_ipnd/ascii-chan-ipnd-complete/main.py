import os
import re
import sys
import urllib2
from xml.dom import minidom
from string import letters
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
	autoescape = True)

art_key = db.Key.from_path('ASCIIChan', 'arts')

def console(s):
	"""Writes an error message (s) to the console."""
	sys.stderr.write('%s\n' % s)

console(art_key)

class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
  	self.response.write(*a, **kw)

  def render_str(self, template, **params):
  	t = jinja_env.get_template(template)
  	return t.render(params)

  def render(self, template, **kw):
  	self.write(self.render_str(template, **kw))

# IP_URL = "http://api.hostip.info/?ip="
def get_latlon():
	IP_API = "http://ip-api.com/xml"
	print "IP_API = " + str(IP_API)
	content = None
	try:
		content = urllib2.urlopen(IP_API).read()
	except urllib2.URLError:
		return
	if content:
		d = minidom.parseString(content)
		lon = d.getElementsByTagName("lon")[0].firstChild.nodeValue
		lat = d.getElementsByTagName("lat")[0].firstChild.nodeValue
		print "lon = " + lon
		print "lat = " + lat
		return lat, lon

def get_coords():
		lat, lon = get_latlon()
		return db.GeoPt(lat, lon)

GMAPS_IFRAME = """<iframe width="600" height="450" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/place?q=%s,%s&key=AIzaSyCDeLGKxnZRbeOvGjw4vVv0ye4_4fdssDU" allowfullscreen></iframe>"""
def gmaps_img(points):

	return GMAPS_IFRAME % (get_latlon())

class Art(db.Model):
	title = db.StringProperty(required = True)
	art = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	coords = db.GeoPtProperty()

class MainPage(Handler):
	def render_front(self, error = '', title = '', art = ''):
		arts = db.GqlQuery(
			"""SELECT * FROM Art WHERE ANCESTOR IS :1 ORDER BY created LIMIT 100""", art_key)

		# this is for quering only one time per render.
		arts = list(arts)

		points = []
		for a in arts:
			if a.coords:
				points.append(a.coords)

		img_url = None
		if points:
			img_url = gmaps_img(points)

		coLat, coLon = get_latlon()

		self.render('front.html', title=title, art=art, error=error, arts=arts, img_url = img_url, coLon= coLon, coLat=coLat)

	def get(self):
		return self.render_front()

	def post(self):
		title = self.request.get('title')
		art = self.request.get('art')
		if title and art:
			p = Art(parent = art_key, title=title, art=art)
			coords = get_coords()
			if coords:
				p.coords = coords
			p.put()
			self.redirect('/')
		else:
			error = "we need both a title and some artwork!"
			self.render_front(error=error, title=title, art=art)

app = webapp2.WSGIApplication([('/', MainPage)], debug = True)
