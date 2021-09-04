from typing import List
from ..database import movie_db
from ..models.models import Movie

def popular() -> List[Movie]:
    return movie_db.lista_popular()

def search_movie(movie_: Movie) -> List[Movie]:
    return movie_db.search(movie_)

def movie(movie_: Movie) -> Movie:
    return movie_db.movie(movie_)

def similiares(movie_: Movie) -> Movie:
    return movie_db.get_similar(movie_)