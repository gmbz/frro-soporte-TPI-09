from typing import List
from ..models.models import Movie, Genero, Person
from . import movie_api


def popular(pag: str) -> List[Movie]:
    listado_popular = movie_api.lista_popular(pag)
    return listado_popular


def search_movie(movie_: Movie) -> List[Movie]:
    return movie_api.search(movie_)


def movie(movie_: Movie) -> Movie:
    return movie_api.movie(movie_)


def get_recommendations(movie_: Movie) -> List[Movie]:
    return movie_api.recommendations(movie_)


def get_movie_credits(movie_: Movie) -> List[Person]:
    return movie_api.movie_credits(movie_)


def get_by_genre(genre_: Genero, pag: str) -> List[Movie]:
    genres = movie_api.get_genres()
    for g in genres:
        if genre_.nombre == g.nombre:
            genre_.id = g.id
            break
    listado_peliculas = movie_api.get_by_genre(genre_, pag)
    return listado_peliculas


def trending_day() -> List[Movie]:
    return movie_api.trending_day()


def top_rated(pag: str) -> List[Movie]:
    listado_popular = movie_api.top_rated(pag)
    return listado_popular


def upcoming(pag: str) -> List[Movie]:
    listado_upcoming = movie_api.upcoming(pag)
    return listado_upcoming
