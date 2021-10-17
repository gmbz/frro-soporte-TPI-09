from typing import List
import requests

from ..models.models import Movie, Person, Serie

api_key = '25398bd0f8e1460f3769b59bfbf5eea6'


def search(person: Person) -> List[Person]:
    """
    Devuelve listado de personas dado un nombre.
    """

    query = (requests.get(
        "https://api.themoviedb.org/3/search/person?api_key=" +
             api_key+"&language=es-ES&include_adult=false&query="+person.nombre
             )).json()
    lista = []
    for data in query['results']:
        per = Person(id=data['id'],
                     nombre=data['name'])
        if data['profile_path']:
            per.perfil = ("https://image.tmdb.org/t/p/original/" +
                          data['profile_path'])
        lista.append(per)
    return lista


def lista_popular(pag: str) -> List[Person]:
    """
    Devuelve lista de personas populares.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/person/popular?api_key=" +
             api_key+"&language=es-ES&page="+pag)).json()
    lista = []
    for data in query['results']:
        per = Person(id=data['id'],
                     nombre=data['name'])
        if data['profile_path']:
            per.perfil = ("https://image.tmdb.org/t/p/original/" +
                          data['profile_path'])
        lista.append(per)
    return lista


def get_person(person_: Person) -> Person:
    """
    Devuelve instancia de persona dado su id.
    """
    id_ = str(person_.id)
    query = (requests.get("https://api.themoviedb.org/3/person/"+id_ +
             "?api_key="+api_key+"&language=es-ES")).json()
    per = Person(id=query['id'],
                 nombre=query['name'],
                 perfil=("https://image.tmdb.org/t/p/original/" +
                         query['profile_path']),
                 fecha_nacimiento=query['birthday'],
                 biografia=query['biography'])
    movie_credits(per)
    serie_credits(per)
    return per


def movie_credits(person_: Person) -> None:
    """
    Setea las peliculas en las que participó la persona.
    """
    id_ = str(person_.id)
    query = (requests.get("https://api.themoviedb.org/3/person/"+id_ +
                          "/movie_credits?api_key="+api_key +
                          "&language=es-ES")).json()
    for data in query['cast']:
        if data['poster_path']:
            peli = Movie(id=data['id'],
                         titulo=data['title'],
                         portada=("https://image.tmdb.org/t/p/w500/" +
                                  data['poster_path']))
            person_.peliculas.append(peli)


def serie_credits(person_: Person) -> None:
    """
    Setea las series en las que participó la persona.
    """
    id_ = str(person_.id)
    query = (requests.get("https://api.themoviedb.org/3/person/"+id_ +
                          "/tv_credits?api_key="+api_key +
                          "&language=es-ES")).json()
    for data in query['cast']:
        if data['poster_path']:
            serie = Serie(id=data['id'],
                          nombre=data['name'],
                          portada=("https://image.tmdb.org/t/p/w500/" +
                                   data['poster_path']))
            person_.series.append(serie)
