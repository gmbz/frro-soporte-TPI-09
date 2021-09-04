from app.database.movie_db import movie
from ..models.models import Comentario, Movie
from .db import session

from typing import List

def create(comment_: Comentario):
    session.add(comment_)
    session.commit()

def list_by_movie(movie_: Movie) -> List[Comentario]:
    return session.query(Comentario).filter(Comentario.id_pelicula == movie_.id)