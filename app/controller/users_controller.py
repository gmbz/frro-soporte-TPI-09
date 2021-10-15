from typing import Optional

from sqlalchemy.sql.functions import current_user

from ..database import user_db
from ..helpers import helper
from ..models.exceptions import UserNotValid, UserAlreadyExists, UserNotFound
from ..models.models import Usuario


def register_user(user_: Usuario) -> Usuario:
    try:
        if helper.validate_registration(user_):
            user_.set_password(user_.password)
            new_user = user_db.register_user(user_)
            return new_user
    except UserNotValid as exc:
        return exc
    except UserAlreadyExists as exc:
        return exc


def autenticacion(username_: str, pass_: str) -> Usuario:
    try:
        user = user_db.autenticacion(username_, pass_)
        return user
    except UserNotFound as exc:
        return exc


def buscar_id(id_usuario: int) -> Optional[Usuario]:
    return user_db.buscar_id(id_usuario)
