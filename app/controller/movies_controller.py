from typing import List
from ..database import movie_db
from ..models.models import Movie, Genero, Person


def popular(pag: str) -> List[Movie]:
    paginas = calcula_paginas(pag)
    listado_popular = movie_db.lista_popular(pag)
    return listado_popular, paginas


def search_movie(movie_: Movie) -> List[Movie]:
    return movie_db.search(movie_)


def movie(movie_: Movie) -> Movie:
    return movie_db.movie(movie_)


def similiares(movie_: Movie) -> List[Movie]:
    return movie_db.get_similar(movie_)


def get_recommendations(movie_: Movie) -> List[Movie]:
    return movie_db.recommendations(movie_)


def get_movie_credits(movie_: Movie) -> List[Person]:
    return movie_db.movie_credits(movie_)


def get_by_genre(genre_: Genero, pag: str) -> List[Movie]:
    genres = movie_db.get_genres()
    for g in genres:
        if genre_.nombre == g.nombre:
            genre_.id = g.id
            break
    paginas = calcula_paginas(pag)
    listado_peliculas = movie_db.get_by_genre(genre_, pag)
    return listado_peliculas, paginas


def trending_day() -> List[Movie]:
    lista = movie_db.trending_day()
    return generador_listas(lista)


def top_rated(pag: str) -> List[Movie]:
    paginas = calcula_paginas(pag)
    listado_popular = movie_db.top_rated(pag)
    return listado_popular, paginas


def upcoming(pag: str) -> List[Movie]:
    paginas = calcula_paginas(pag)
    listado_upcoming = movie_db.upcoming(pag)
    return listado_upcoming, paginas


def generador_listas(lista):

    def generador(initial: int = 0):
        while True:
            _lista = []
            for movie in lista:
                _lista.append(movie)
                initial += 1
                if initial in (5, 10, 15, 20):
                    yield _lista
                    _lista = []
    g = generador()
    listado = []
    for _ in range(4):
        _listado = next(g)
        listado.append(_listado)
    return listado


def calcula_paginas(pag: str):
    """Calcula los numeros que se van a mostrar en la paginación.
    """
    n = int(pag)
    resta = 3
    r = 2
    for i in range(1, 3+1):
        if n == i:
            resta -= r
            break
        r-1
    lista = []
    for p in range(n-resta, n+4):
        lista.append(str(p))
    prev_pag = str(n-1)
    next_pag = str(n+1)
    return lista, prev_pag, next_pag
