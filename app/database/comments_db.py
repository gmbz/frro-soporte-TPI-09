from ..models.models import Comentario, Movie, Serie
from .db import session

from typing import List


def create(comment_: Comentario):
    session.add(comment_)
    session.commit()


def list_by_movie(movie: Movie) -> List[Comentario]:
    return session.query(Comentario).filter(
        Comentario.id_pelicula == movie.id).order_by(Comentario.fecha.desc())


def list_by_serie(serie: Serie) -> List[Comentario]:
    return session.query(Comentario).filter(
        Comentario.id_serie == serie.id).order_by(Comentario.fecha.desc())
