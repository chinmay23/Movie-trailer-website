# importing the fresh_tomatoes file
import fresh_tomatoes

# importing the media file consisting of __init__ function
import media

# list of objects(movies)

dunkirk = media.Movie(
    "Dunkirk", """In May 1940, Germany advanced into France
    trapping Allied troops on the beaches of Dunkirk.
    At the end of this heroic mission, 330, 000 French,
    British, Belgian and Dutch soldiers were safely
    evacuated.""",
    """https://en.wikipedia.org/wiki/
    Dunkirk_(2017_film)#/media/File:Dunkirk_Film_poster.jpg""",
    "https://www.youtube.com/watch?v=F-eMt3SrfFU"
)


dark_knight_rises = media.Movie(
    "The Dark Knight Rises", """It has been eight
    years since Batman(Christian Bale),
    in collusion with Commissioner Gordon
    (Gary Oldman), vanished into the night.
    However, the arrival of a cunning cat
    burglar(Anne Hathaway) and a merciless
    terrorist named Bane(Tom Hardy) force
    Batman out of exile and into a battle
    he may not be able to win.""",
    """https://images-na.ssl-images-amazon.com/
    images/I/711IkMGkWtL._SY550_.jpg""",
    "https://www.youtube.com/watch?v=g8evyE9TuYk"
)

rush = media.Movie(
    "Rush", """In the mid - 1970s, charismatic English playboy
    James Hunt(Chris Hemsworth) and Austrian perfectionist
    Niki Lauda(Daniel Brühl) share an intense rivalry in
    Formula 1 racing. Meanwhile, the women(Olivia Wilde)
    as both drivers risk death with every lap.""",
    """https://d32qys9a6wm9no.cloudfront.net/images/movies/
    poster/08/08aee6276db142f4b8ac98fb8ee0ed1b_500x735.jpg?t=1488656061""",
    "https://www.youtube.com/watch?v=9ZJqxgR-5Xc"
)

fight_club = media.Movie(
    "Fight Club", """A depressed man(Edward Norton)
    suffering from insomnia meets a strange soap
    salesman named Tyler Durden(Brad Pitt) and
    soon finds himself living in his squalid house
    after his perfect apartment is destroyed.
    Their perfect partnership frays when Marla
    a fellow support group crasher, attracts
    Tyler's attention.""",
    """https://images-na.ssl-images-amazon.com/
    images/I/51OsUdPrjoL.jpg""",
    "https://www.youtube.com/watch?v=_XgQA9Ab0Gw"
)


captain_phillips = media.Movie(
    "Captain Phillips", """In April 2009,
    the U.S. containership Maersk Alabama
    sails toward its destination on a day
    that seems like any other. The pirates
    are after millions of dollars, and
    Phillips must use his wits to make
    sure everyone survives and returns
    home safely.""",
    """http://cdn.collider.com/wp-content/
    uploads/captain-phillips-poster.jpg""",
    "https://www.youtube.com/watch?v=u7JptS2VZNg"
)

# Array of objects(movies)
movies = [
    dunkirk,
    dark_knight_rises,
    rush,
    fight_club,
    captain_phillips
]

# Function call for opening browser having list of movies
fresh_tomatoes.open_movies_page(movies)
