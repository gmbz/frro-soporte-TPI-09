from typing import List
import datetime

from ..database import comments_db, user_db, serie_db, movie_db
from ..models.models import Movie, Comentario, Serie, Usuario
from . import movie_api, serie_api


def registrar_comentario(comment: Comentario, movie_: Movie, user: Usuario):
    user = user_db.buscar_id_user(user)
    movie = movie_db.get_in_db(movie_)
    date_ = datetime.datetime.now()
    date_string = date_.strftime("%d/%m/%Y %H:%M")
    comment.fecha = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
    if movie is None:
        movie = movie_api.movie_without_genre(movie_)
    user.comments.append(comment)
    movie.comments.append(comment)
    comments_db.create(comment)


def lista_por_pelicula(movie_: Movie) -> List[Comentario]:
    return comments_db.list_by_movie(movie_)


def reg_comment(com: Comentario, serie_: Serie, user_: Usuario):
    user = user_db.buscar_id(user_.id)
    serie = serie_db.get_in_db(serie_)
    date_ = datetime.datetime.now()
    date_string = date_.strftime("%d/%m/%Y %H:%M")
    com.fecha = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
    if serie is None:
        serie = serie_api.details(serie_.id)
    user.comments.append(com)
    serie.comments.append(com)
    comments_db.create(com)


def lista_por_serie(serie: Serie) -> List[Serie]:
    return comments_db.list_by_serie(serie)
