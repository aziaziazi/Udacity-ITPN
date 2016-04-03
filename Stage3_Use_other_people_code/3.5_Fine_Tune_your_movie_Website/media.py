#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Fine tune the movie website

# Video class
# Ajouter année ?
class Video():
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url #should be youtube url


# Movie class
class Movie(Video):
	def __init__(self, title, poster_image_url, trailer_youtube_url, director):
		Video.__init__(self, title, poster_image_url, trailer_youtube_url)
		self.director = director

# Tv_show class
class Tv_show(Video):
	def __init__(self, title, poster_image_url, trailer_youtube_url, saison, epidode):
		Video.__init__(self, title, poster_image_url, trailer_youtube_url)
		self.saison = saison
		self.epidode = epidode