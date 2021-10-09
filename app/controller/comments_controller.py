from typing import List
from ..database import comments_db, user_db, movie_db
from ..models.models import Movie, Comentario, Usuario


def registrar_comentario(comment: Comentario, movie_: Movie, id_user: int):
    user = user_db.buscar_id(id_user)
    movie = movie_db.get_in_db(movie_)
    if movie is None:
        movie = movie_db.movie_without_genre(movie_)
    user.comments.append(comment)
    movie.comments.append(comment)
    print(comment.contenido)
    comments_db.create(comment)


def lista_por_pelicula(movie_: Movie) -> List[Comentario]:
    return comments_db.list_by_movie(movie_)
