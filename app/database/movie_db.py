from typing import Optional

from ..models.models import Movie
from .db import session


def get_in_db(movie_: Movie) -> Optional[Movie]:
    """
    Devuelve la instancia de la pelicula guardada en la base de dados dado
    su id.
    """
    return session.query(Movie).get(movie_.id)
