from typing import List
from ..database import comments_db, user_db, movie_db
from ..models.models import Movie, Comentario, Genero, Usuario

def registrar_comentario(comment_: Comentario, movie_: Movie, user_: Usuario):
    user = user_db.buscar_id_user(user_)
    movie = movie_db.get_in_db(movie_)
    if movie is None:
        movie = movie_db.movie(movie_)
    user.comments.append(comment_)
    movie.comments.append(comment_)
    comments_db.create(comment_)

def lista_por_pelicula(movie_: Movie) -> List[Comentario]:
    return comments_db.list_by_movie(movie_)