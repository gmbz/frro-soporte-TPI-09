import re

from ..models.models import Usuario

from ..models.exceptions import UserNotValid


def __email_is_valid(email: str) -> bool:
    if not isinstance(email, str):
        return False
    regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    return bool(re.search(regex, email))


def __username_is_valid(username: str) -> bool:
    if 6 <= len(username) <= 30:
        regex = r'^\w+$'
        return bool(re.search(regex, username))
    return False


def __password_is_valid(password: str) -> bool:
    if 8 <= len(password) <= 16:
        regex = r'^([a-zA-Z]|\d)+$'
        return bool(re.search(regex, password))
    return False


def validate_registration(user_: Usuario) -> bool:
    """
    Valida la longitud y caracteres de el username, contraseña y email.
    :type user_: Usuario
    :raise: UserNotValid
    :rtype: bool
    """
    if not __email_is_valid(user_.email):
        raise UserNotValid('Email invalido')
    if not __username_is_valid(user_.username):
        raise UserNotValid('Nombre de usuario invalido')
    if not __password_is_valid(user_.password):
        raise UserNotValid('Contraseña invalida')
    return True
