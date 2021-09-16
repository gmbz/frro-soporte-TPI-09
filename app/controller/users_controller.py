from typing import Optional
from ..database import user_db
from ..models.models import Usuario


def register_user(user_: Usuario) -> Usuario:
    return user_db.register_user(user_)


def autenticacion(username_: str, pass_: str) -> Usuario:
    return user_db.autenticacion(username_, pass_)


def buscar_id(id_usuario: int) -> Optional[Usuario]:
    return user_db.buscar_id(id_usuario)
