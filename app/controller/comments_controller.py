from typing import List
from ..database import comments_db
from ..models.models import Movie, Comentario, Genero, Usuario

from ..database.db import session

def registrar_comentario(comment_: Comentario):
    comments_db.create(comment_)

def lista_por_pelicula(movie_: Movie) -> List[Comentario]:
    return comments_db.list_by_movie(movie_)