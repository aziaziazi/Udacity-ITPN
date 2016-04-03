import webbrowser

class Movie():

	def __init__(self, title, trailer):
		self.title = title
		self.trailer = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer)