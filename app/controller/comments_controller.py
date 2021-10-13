from typing import List
import datetime

from ..database import comments_db, user_db, movie_db
from ..models.models import Movie, Comentario


def registrar_comentario(comment: Comentario, movie_: Movie, id_user: int):
    user = user_db.buscar_id(id_user)
    movie = movie_db.get_in_db(movie_)
    date_ = datetime.datetime.now()
    date_string = date_.strftime("%d/%m/%Y %H:%M")
    comment.fecha = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
    if movie is None:
        movie = movie_db.movie_without_genre(movie_)
    user.comments.append(comment)
    movie.comments.append(comment)
    comments_db.create(comment)


def lista_por_pelicula(movie_: Movie) -> List[Comentario]:
    return comments_db.list_by_movie(movie_)
