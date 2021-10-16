from typing import List, Iterable, Optional
import requests
import datetime

from ..models.models import Genero, Movie, Person
from .db import session


api_key = "25398bd0f8e1460f3769b59bfbf5eea6"


def lista_popular(pag: str) -> List[Movie]:
    """
    Devuelve lista de peliculas populares.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/movie/popular?api_key="+api_key +
        "&language=es-ES&page="+pag)).json()
    lista = []
    set_movie_list(lista, query)
    return lista


def search(movie_: Movie) -> List[Movie]:
    """
    Devuelve la instancia de la pelicula dado su titulo.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/search/movie?api_key=" +
        api_key+"&language=es-ES&query="+movie_.titulo)).json()
    lista = []
    set_movie_list(lista, query)
    return lista


def movie(movie_: Movie) -> Movie:
    """
    Devuelve la instancia de la pelicula dado su id.
    """
    id_ = str(movie_.id)
    query = (requests.get("https://api.themoviedb.org/3/movie/" +
             id_+"?api_key="+api_key+"&language=es-ES")).json()
    genres = query['genres']
    peli = Movie(id=query['id'],
                 titulo=query['title'],
                 descripcion=query['overview'],
                 pagina_principal=query['homepage'],
                 valoracion=int(query['vote_average']*10),
                 portada="https://image.tmdb.org/t/p/w500/" +
                 query['poster_path'],
                 fecha_date=datetime.datetime.strptime(
                     query['release_date'], "%Y-%m-%d"),
                 video=get_video(id_))
    set_fecha(peli)
    set_genre(peli, genres)
    return peli


def movie_without_genre(movie_: Movie) -> Movie:
    """
    Devuelve la instancia de la pelicula, sin generos, dado su id.
    """
    id_ = str(movie_.id)
    query = (requests.get("https://api.themoviedb.org/3/movie/" +
             id_+"?api_key="+api_key+"&language=es-ES")).json()
    peli = Movie(id=query['id'],
                 titulo=query['title'],
                 descripcion=query['overview'],
                 valoracion=int(query['vote_average']*10),
                 portada="https://image.tmdb.org/t/p/w500/" +
                 query['poster_path'],
                 fecha_date=datetime.datetime.strptime(
                     query['release_date'], "%Y-%m-%d"),
                 video=get_video(id_))
    set_fecha(peli)
    return peli


def get_by_genre(genre_: Genero, pag: str) -> List[Movie]:
    """
    Devuelve listado de todas las peliculas dado un genero.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/discover/movie?api_key="+api_key +
        "&language=es-ES&page="+pag+"&sort_by=popularity.desc&with_genres=" +
        str(genre_.id))).json()
    lista = []
    set_movie_list(lista, query)
    return lista


def get_genres() -> List[Genero]:
    """Devuelve lista de generos.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/genre/movie/list?api_key=" +
        api_key+"&language=es-ES")).json()
    lista = []
    for g in query['genres']:
        _genre = Genero(id=g['id'], nombre=g['name'])
        lista.append(_genre)
    return lista


def trending_day() -> List[Movie]:
    """
    Devuelve lista de las peliculas en tendencias de hoy.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/trending/movie/day?api_key=" +
        api_key+"&language=es-ES")).json()
    lista = []
    set_movie_list(lista, query)
    return lista


def top_rated(pag: str) -> List[Movie]:
    """
    Devuelve lista del top de peliculas.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/movie/top_rated?api_key="+api_key +
        "&language=es-ES&page="+pag)).json()
    lista = []
    set_movie_list(lista, query)
    return lista


def upcoming(pag: str) -> List[Movie]:
    """
    Devuelva listado de los proximos estrenos.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/discover/movie?api_key="+api_key +
             "&language=es-ES&sort_by=popularity.desc&page="+pag +
             "&primary_release_date.gte=2021-10-10&" +
             "primary_release_date.lte=2021-12-30&year=2021")).json()
    lista = []
    set_movie_list(lista, query)
    return lista


def recommendations(movie_: Movie) -> List[Movie]:
    """
    Devuelve listado de peliculas recomendadas dado una pelicula.
    """
    query = (requests.get("https://api.themoviedb.org/3/movie/"+str(movie_.id)
                          + "/recommendations?api_key="+api_key +
                          "&language=es-ES")).json()
    lista = []
    set_movie_list(lista, query)
    return lista


def movie_credits(movie_: Movie) -> List[Person]:
    """
    Devuelve listado que contiene el reparto de la pelicula.
    """
    query = (requests.get("https://api.themoviedb.org/3/movie/" +
             str(movie_.id)+"/credits?api_key="+api_key)).json()
    lista = []
    for data in query['cast']:
        if data['profile_path']:
            per = Person(id=data['id'],
                         nombre=data['name'],
                         perfil="https://image.tmdb.org/t/p/original/" +
                         data['profile_path'])
            lista.append(per)
    return lista


def set_movie_list(lista: Iterable, query) -> None:
    """
    Genera la lista de peliculas.
    """
    for data in query['results']:
        peli = Movie(id=data['id'],
                     titulo=data['title'],
                     descripcion=data['overview'],
                     valoracion=int(data['vote_average']*10),)
        if data['poster_path']:
            peli.portada = "https://image.tmdb.org/t/p/original/" + \
                data['poster_path']
        if data['release_date']:
            peli.fecha_date = datetime.datetime.strptime(data['release_date'],
                                                         "%Y-%m-%d")
            set_fecha(peli)
        lista.append(peli)


def set_movie(movie: Movie) -> None:
    """
    Setea los datos de una pelicula.
    """
    query = (requests.get("https://api.themoviedb.org/3/movie/" +
             str(movie.id)+"?api_key="+api_key+"&language=es-ES")).json()
    movie.titulo = query['title']
    movie.descripcion = query['overview']
    movie.portada = "https://image.tmdb.org/t/p/w500/" + query['poster_path']
    movie.fecha = query['release_date']


def set_fecha(peli: Movie) -> None:
    """
    Setea la fecha que se mostrará en la web.
    """
    peli.fecha_string = peli.fecha_date.strftime("%d %b %Y")


def set_genre(movie_: Movie, genres_: Iterable[dict]):
    """
    Setea los generos de una pelicula dado su id.
    """
    for _ in genres_:
        genre = Genero(id=_['id'], nombre=_['name'])
        movie_.generos.append(genre)


def get_video(id_: str) -> Optional[str]:
    """
    Devuelve la direccion del trailer de youtube dado su id.
    Devuelve None si no encuentra nada.
    """
    try:
        query = (requests.get("https://api.themoviedb.org/3/movie/" +
                              id_+"/videos?api_key="+api_key)).json()
        if query['results']:
            for data in query['results']:
                if data['type'] == 'Trailer':
                    video = data['key']
                    break
        return video
    except:
        return None
