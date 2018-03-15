import webbrowser


class Video():
    """ This class store the base information of a video """
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """ This class store a movie information """

    def __init__(self, title, duration, storyline, poster_image, trailer_url):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image = poster_image
        self.url = trailer_url
