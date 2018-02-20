import webbrowser

# Define Movie class


class Movie():
    """Movie class displays a static webpage displaying list of movies.
       Consists of properties of movies: title,storyline,poster,URL of trailer
       Creates reference to current instance of class,accessing attributes and
       methods of class entertainment.

        Attributes:
                  title: Title of the movie
                  storyline: Storyline of the movie
                  poster_image_url: Poster of the movie
                  trailer_youtube_url: URL of the movie trailer
        Arguements:
                  movie_title: Title of the movie
                  movie_storyline: Storyline of the movie
                  poster_image: Poster of the movie
                  trailer: URL of the movie trailer
        Methods:
                 show_trailer: Opens webbrowser for playing trailer after
                 clicking on specific movie trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """"  Opens webbrowser for playing trailer after
              clicking on specific movie trailer.
        """

        webbrowser.open(self.trailer_youtube_url)
