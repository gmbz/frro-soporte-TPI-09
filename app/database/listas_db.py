from ..models.models import MisListas, MisListasMovie, MisListasSerie, Serie, Usuario, Movie
from .db import session

from typing import List


def create(mi_lista: MisListas) -> MisListas:
    session.add(mi_lista)
    session.commit()
    return mi_lista


def delete(mi_lista: MisListas) -> int:
    # BORRAR LAS SERIES Y PELICULAS RELACIONADAS A LA LISTA
    session.query(MisListasMovie).filter(
        MisListasMovie.id_lista == mi_lista.id).delete()
    session.query(MisListasSerie).filter(
        MisListasSerie.id_lista == mi_lista.id).delete()
    # BORRAR LA LISTA Y DEVUELVE LA CANTIDAD DE FILAS AFECTADAS
    rows = session.query(MisListas).filter(
        MisListas.id == mi_lista.id).delete()
    session.commit()
    return rows


def delete_serie(lista_serie: MisListasSerie, serie_: Serie) -> MisListasSerie:
    session.query(MisListasSerie).filter(
        MisListasSerie.id_serie == serie_.id).delete()
    session.commit()
    return lista_serie


def delete_movie(lista_movie: MisListasMovie, movie_: Movie) -> MisListasMovie:
    session.query(MisListasMovie).filter(
        MisListasMovie.id_movie == movie_.id).delete()
    session.commit()
    return lista_movie


def get_mis_listas_serie(mi_lista: MisListas) -> MisListasSerie:
    return session.query(MisListasSerie).filter(
        MisListasSerie.id_lista == mi_lista.id).first()


def get_mis_listas_movie(mi_lista: MisListas) -> MisListasMovie:
    return session.query(MisListasMovie).filter(
        MisListasMovie.id_lista == mi_lista.id).first()


def get_by_id(mi_lista: MisListas) -> MisListas:
    return session.query(MisListas).get(mi_lista.id)


def get_by_user(user: Usuario) -> List[MisListas]:
    return session.query(MisListas).filter(MisListas.id_user == user.id)


def commit_db() -> None:
    session.commit()
