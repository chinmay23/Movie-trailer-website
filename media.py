import webbrowser

# Define Movie class


class Movie():
    # Movie class displays a static webpage displaying list of movies

    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        # Reference to current instance of class, accessing the attributes and
        # methods of class entertainment
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
    # Opens webbrowser for playing trailer after clicking on specific movie
    # poster

    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
