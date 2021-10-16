import re
import requests
import json

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


def is_human(captcha, current_app) -> bool:
    """
    Valida la recaptcha response del servidor de Google.
    :return: bool
    """
    payload = {'response': captcha,
               'secret': current_app.config['RECAPTCHA_PRIVATE_KEY']}
    response = requests.post(
        "https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']


def calcula_paginas(pag: str):
    """
    Calcula los numeros que se van a mostrar en la paginación.
    """
    n = int(pag)
    resta = 3
    r = 2
    for i in range(1, 3+1):
        if n == i:
            resta -= r
            break
        r-1
    lista = []
    for p in range(n-resta, n+4):
        lista.append(str(p))
    prev_pag = str(n-1)
    next_pag = str(n+1)
    return lista, prev_pag, next_pag
