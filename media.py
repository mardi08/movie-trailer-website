import webbrowser


class Video():
    """ This class store the base information of a video.

    Attributes:
        title (str): the title of the movie.
        duration (str): the duration of the trailer video.
    """
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """ This class store a movie information.

    Attributes:
        title (str): the title of the movie.
        duration (str): the duration of the trailer video.
        storyline (str): a brief description of the movie storyline.
        poster_image (str): a path or url to the poster image of the movie.
        trailer_url (str): a path or url to the movie trailer video.
    """

    def __init__(self, title, duration, storyline, poster_image, trailer_url):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image = poster_image
        self.url = trailer_url
