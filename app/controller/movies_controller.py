from typing import List
from ..database import movie_db
from ..models.models import Movie, Genero


def popular() -> List[Movie]:
    return movie_db.lista_popular()


def search_movie(movie_: Movie) -> List[Movie]:
    return movie_db.search(movie_)


def movie(movie_: Movie) -> Movie:
    return movie_db.movie(movie_)


def similiares(movie_: Movie) -> Movie:
    return movie_db.get_similar(movie_)


def get_by_genre(genre_: Genero) -> List[Movie]:
    genres = movie_db.get_genres()
    for g in genres:
        if genre_.nombre == g.nombre:
            genre_.id = g.id
            break
    return movie_db.get_by_genre(genre_)


def trending_day() -> List[Movie]:
    return movie_db.trending_day()


def top_rated() -> List[Movie]:
    return movie_db.top_rated()
