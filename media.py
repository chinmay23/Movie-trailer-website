import webbrowser


class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        # Attributes of movies
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        # Opens webbrowser for playing trailer
        webbrowser.open(self.trailer_youtube_url)
