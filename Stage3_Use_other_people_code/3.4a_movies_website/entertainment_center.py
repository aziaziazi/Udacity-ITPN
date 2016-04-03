# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

rubber = media.Movie("Rubber",
												"A tire, which has psychokinetics powers, begins a frenetic serial killing in the californian desert.",
												"https://oddityfarm.files.wordpress.com/2012/05/rubber-gooood-front.jpg",
												"https://youtu.be/6G5pyFhmAqE?t=8s")

the_lobster = media.Movie("The Lobster",
													"A guy try to not being in couple.",
													"http://www.clapmag.com/wp-content/uploads/2015/05/The-Lobster.jpg",
													"https://www.youtube.com/watch?v=bemcHBqng4o")

budapest_hotel = media.Movie("The Grand Budapest Hotel",
															"the adventures of Gustave who search for a stolen painting",
															"http://www.rfplnj.org/sites/default/files/images/featuredmovies/grand%20budapest%20hotel.jpg",
															"https://www.youtube.com/watch?v=1Fg5iWmQjwk")

# print (the_lobster.trailer_youtube_url)
# print(rubber.storyline)
# print (the_lobster.storyline)
# rubber.show_trailer()

# rubber.show_trailer()

movies = [rubber, the_lobster, budapest_hotel]
fresh_tomatoes.open_movies_page(movies)

