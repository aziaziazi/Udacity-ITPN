## Fine tune the movie website
## To do next : add series in the site

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

# creat movies instances
reality = media.Movie("Reality",
											"http://fr.web.img5.acsta.net/pictures/14/12/16/17/20/077619.jpg",
											"https://www.youtube.com/watch?v=UbEqPsq8PyY",
											"Quentin Dupieux")

gravity = media.Movie("Gravity",
											"http://fr.web.img1.acsta.net/pictures/210/232/21023233_20130729173134181.jpg",
											"https://www.youtube.com/watch?v=OiTiKOy59o4",
											"Alfonso Cuarón")

oncle_amerique = media.Movie("Mon oncle d'Amérique",
															"http://fr.web.img2.acsta.net/medias/nmedia/00/02/58/34/affiche.jpg",
															"https://www.youtube.com/watch?v=hxXvuvUpjls",
															"Alain Resnais")

# creat tv shows instances
sp101 = media.Tv_show("South Park - Cartman a une sounde anale",
											"http://www.southparkclub.com/pix/season1/Cartman%20Gets%20an%20Anal%20Probe/18.jpg",
											"https://www.youtube.com/watch?v=4DlfHfqJd7g",
											"1",
											"01")

lost203 = media.Tv_show("Lost - 108 minutes",
												"http://images2.fanpop.com/images/photos/5100000/Fictional-Dharma-Initiative-Ads-lost-5152477-682-1024.jpg",
												"https://www.youtube.com/watch?v=72kQIIDBIUU",
												"2",
												"03")

# list movies
movies =  [reality, gravity, oncle_amerique]

# list tv shows
tv_shows = [sp101, lost203]


# Call open_movies_page with movies and tv shows list
fresh_tomatoes.open_movies_page(movies, tv_shows)


