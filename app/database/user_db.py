from ..models.models import Usuario
from .db import session
from ..models.exceptions import UserAlreadyExists, UserNotFound

from typing import Optional


def register_user(usuario: Usuario) -> Usuario:
    """Agrega un nuevo usuario a la tabla y lo devuelve"""
    if user_exists(usuario):
        raise UserAlreadyExists(f"User {usuario.username} ya existe")
    if email_exists(usuario):
        raise UserAlreadyExists(f"El email {usuario.email} ya existe")
    session.add(usuario)
    session.commit()
    return usuario


def buscar_id_user(user_: Usuario) -> Usuario:
    return session.query(Usuario).get(user_.id)


def buscar_id(id_usuario) -> Optional[Usuario]:
    return session.query(Usuario).get(id_usuario)


def user_exists(user_: Usuario) -> Optional[Usuario]:
    return session.query(Usuario).filter(Usuario.username == user_.username
                                         ).first()


def email_exists(user_: Usuario) -> Optional[Usuario]:
    return session.query(Usuario).filter(Usuario.email == user_.email
                                         ).first()


def buscar_user(username_: str) -> Optional[Usuario]:
    return session.query(Usuario).filter(Usuario.username == username_).first()


def autenticacion(username_: str, pass_: str) -> Optional[Usuario]:
    usuario = buscar_user(username_)
    if usuario:
        check = usuario.check_password(pass_)
        if check is True:
            return usuario
        raise UserNotFound('Contraseña incorrecta')
    raise UserNotFound('El usuario no existe')


def change_pass():
    session.commit()
