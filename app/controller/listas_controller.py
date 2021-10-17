from typing import List

from ..database import listas_db, user_db, serie_db, movie_db
from ..models.models import Movie, Serie, Usuario, MisListas
from . import movie_api, serie_api


def crear_lista(mi_lista: MisListas, user_: Usuario) -> MisListas:
    user = user_db.buscar_id_user(user_)
    user.listas.append(mi_lista)
    return listas_db.create(mi_lista)


def borrar_lista(mi_lista: MisListas) -> int:
    return listas_db.delete(mi_lista)


def add_movie(mi_lista: MisListas, movie_: Movie) -> MisListas:
    lista = listas_db.get_by_id(mi_lista)
    movie = movie_db.get_in_db(movie_)
    if movie is None:
        movie = movie_api.movie_without_genre(movie_)
    lista.peliculas.append(movie)
    listas_db.commit_db()
    return lista


def add_serie(mi_lista: MisListas, serie_: Serie) -> MisListas:
    lista = listas_db.get_by_id(mi_lista)
    serie = serie_db.get_in_db(serie_)
    if serie is None:
        serie = serie_api.details(serie_.id)
    lista.series.append(serie)
    listas_db.commit_db()
    return lista


def listado_por_usuario(user: Usuario) -> List[MisListas]:
    lista = listas_db.get_by_user(user)
    return lista


def get_list(mi_lista_: MisListas) -> MisListas:
    mi_lista = listas_db.get_by_id(mi_lista_)
    for m in mi_lista.peliculas:
        movie_api.set_movie(m)

    return mi_lista


def borrar_serie(mi_lista_: MisListas, serie: Serie) -> MisListas:
    mi_lista = listas_db.get_by_id(mi_lista_)
    mi_lista_serie = listas_db.get_mis_listas_serie(mi_lista)
    listas_db.delete_serie(mi_lista_serie, serie)
    return mi_lista


def borrar_movie(mi_lista_: MisListas, movie: Serie) -> MisListas:
    mi_lista = listas_db.get_by_id(mi_lista_)
    mi_lista_serie = listas_db.get_mis_listas_serie(mi_lista)
    listas_db.delete_movie(mi_lista_serie, movie)
    return mi_lista
