import fresh_tomatoes
import media

la_perruche = media.Movie("La Perruche", "https://www.youtube.com/watch?v=tq7uw6_viSM")

# la_perruche.show_trailer()

movies = [la_perruche]
fresh_tomatoes.open_movies_page(movies)