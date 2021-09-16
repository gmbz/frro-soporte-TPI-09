from typing import List
import requests

from ..models.models import Person

api_key = '25398bd0f8e1460f3769b59bfbf5eea6'


def lista_popular() -> List[Person]:

    query = (requests.get(
        "https://api.themoviedb.org/3/person/popular?api_key=" +
             api_key+"&language=es-ES&page=1")).json()
    lista = []
    for data in query['results']:
        per = Person(id=data['id'],
                     nombre=data['name'])
        if data['profile_path']:
            per.perfil = ("https://image.tmdb.org/t/p/original/" +
                          data['profile_path'])
        lista.append(per)
    return lista
