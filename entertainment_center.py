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
                        "https://images-na.ssl-images-amazon.com/images/I/71oka2eUBvL._SY550_.jpg",
                        "https://www.youtube.com/watch?v=sutgWjz10sM")

insurgent = media.Movie("Insurgent",
                        "00:02:24",
                        "Divergent second series",
                        "https://78.media.tumblr.com/62c661765053875f6cbb7f2f1c22c52f/tumblr_niwixp4aBR1siuwieo1_500.png",
                        "https://www.youtube.com/watch?v=suZcGoRLXkU")

allegiant = media.Movie("Allegiant",
                        "00:02:23",
                        "divergent third series",
                        "http://www.impawards.com/2016/posters/divergent_series_allegiant_ver17.jpg",
                        "https://www.youtube.com/watch?v=0G0C-vMHcQY")

hungerGames = media.Movie("The Hunger Games, Mockingjay Part 2",
                          "00:02:35",
                          "HungerGames series Mockingjay part2",
                          "https://image.tmdb.org/t/p/original/w93GAiq860UjmgR6tU9h2T24vaV.jpg",
                          "https://www.youtube.com/watch?v=n-7K_OjsDCQ")

last_jedi = media.Movie("Star Wars, The Last Jedi",
                        "00:02:34",
                        "Star Wars, the most recent sequel",
                        "https://lumiere-a.akamaihd.net/v1/images/sb_dolby_worldwide_handout_13x19_v3_lg_use_this_one_cc3cc869.jpeg?region=0%2C0%2C821%2C1200",
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY")

star_trek = media.Movie("Star Trek Beyond",
                        "00:01:34",
                        "Star Trek sequel, released in 2016",
                        "https://3.bp.blogspot.com/-G1tnY29gDuE/V5z9scFBcXI/AAAAAAAARjQ/vD0jjbs35pItz5EpYtJbAG0MWc6od0KZgCLcB/s1600/STBEYOND1.jpg",
                        "https://www.youtube.com/watch?v=XRVD32rnzOw")



# creating an in-order list for the movies instances
movies = [divergent, insurgent, allegiant, hungerGames, last_jedi, star_trek]

# Generate movie trailer website page
fresh_tomatoes.open_movies_page(movies)
