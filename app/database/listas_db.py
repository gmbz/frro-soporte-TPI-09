from ..models.models import MisListas, MisListasMovie, MisListasSerie, Usuario
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


def get_by_id(mi_lista: MisListas) -> MisListas:
    return session.query(MisListas).get(mi_lista.id)


def get_by_user(user: Usuario) -> List[MisListas]:
    return session.query(MisListas).filter(MisListas.id_user == user.id)


def commit_db() -> None:
    session.commit()
