from typing import Optional

from ..models.models import Serie
from .db import session


def get_in_db(serie_: Serie) -> Optional[Serie]:
    """
    Devuelve la instancia de la serie guardada en la base de dados dado
    su id.
    """
    return session.query(Serie).get(serie_.id)
