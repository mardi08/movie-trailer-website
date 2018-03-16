import media
import fresh_tomatoes

# Instances of Favorite Movies that are shown on the
# Movie trailer website page.
# input argument follows the following format:
# (title, duration, storyline, poster_image, trailer_url)
# Note: poster_image and trailer_url are address in string format

divergent = media.Movie("Divergent",
                        "00:02:31",
                        "Divergent first series",
                        "img/divergent.jpg",
                        "https://www.youtube.com/watch?v=sutgWjz10sM")

insurgent = media.Movie("Insurgent",
                        "00:02:24",
                        "Divergent second series",
                        "img/insurgent.png",
                        "https://www.youtube.com/watch?v=suZcGoRLXkU")

allegiant = media.Movie("Allegiant",
                        "00:02:23",
                        "divergent third series",
                        "img/allegiant.jpg",
                        "https://www.youtube.com/watch?v=0G0C-vMHcQY")

hungerGames = media.Movie("The Hunger Games, Mockingjay Part 2",
                          "00:02:35",
                          "HungerGames series Mockingjay part2",
                          "img/hungergames.jpg",
                          "https://www.youtube.com/watch?v=n-7K_OjsDCQ")

last_jedi = media.Movie("Star Wars, The Last Jedi",
                        "00:02:34",
                        "Star Wars, the most recent sequel",
                        "img/starwars.jpeg",
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY")

star_trek = media.Movie("Star Trek Beyond",
                        "00:01:34",
                        "Star Trek sequel, released in 2016",
                        "img/startrek.jpg",
                        "https://www.youtube.com/watch?v=XRVD32rnzOw")

# creating an in-order list for the movies instances
movies = [divergent, insurgent, allegiant, hungerGames, last_jedi, star_trek]

# Generate movie trailer website page
fresh_tomatoes.open_movies_page(movies)
