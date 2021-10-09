from typing import List, Iterable, Optional
import requests

from ..models.models import Genero, Movie
from .db import session


api_key = "25398bd0f8e1460f3769b59bfbf5eea6"


def lista_popular(pag: str) -> List[Movie]:
    """Devuelve lista de peliculas populares.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/movie/popular?api_key="+api_key +
        "&language=es-ES&page="+pag)).json()
    lista = []
    for data in query['results']:
        peli = Movie(id=data['id'],
                     titulo=data['title'],
                     descripcion=data['overview'],
                     portada="https://image.tmdb.org/t/p/original/" +
                     data['poster_path'],
                     fecha=data['release_date'])
        lista.append(peli)
    return lista


def search(movie_: Movie) -> List[Movie]:
    """Devuelve la instancia de la pelicula dado su titulo.
    """
    query = requests.get("https://api.themoviedb.org/3/search/movie?api_key=" +
                         api_key+"&language=es-ES&query="+movie_.titulo)
    j = query.json()
    pelicula = j['results']
    lista = []
    for data in pelicula:
        if data['poster_path']:
            peli = Movie(id=data['id'],
                         titulo=data['title'],
                         descripcion=data['overview'],
                         portada="https://image.tmdb.org/t/p/w500/" +
                         data['poster_path'],
                         fecha=data['release_date'])
            lista.append(peli)
    return lista


def movie(movie_: Movie) -> Movie:
    """Devuelve la instancia de la pelicula dado su id.
    """
    id_ = str(movie_.id)
    query = (requests.get("https://api.themoviedb.org/3/movie/" +
             id_+"?api_key="+api_key+"&language=es-ES")).json()
    genres = query['genres']
    peli = Movie(id=query['id'],
                 titulo=query['title'],
                 descripcion=query['overview'],
                 portada="https://image.tmdb.org/t/p/w500/" +
                 query['poster_path'],
                 fecha=query['release_date'],
                 video=get_video(id_))
    set_genre(peli, genres)
    return peli


def movie_without_genre(movie_: Movie) -> Movie:
    """Devuelve la instancia de la pelicula, sin generos, dado su id.
    """
    id_ = str(movie_.id)
    query = (requests.get("https://api.themoviedb.org/3/movie/" +
             id_+"?api_key="+api_key+"&language=es-ES")).json()
    peli = Movie(id=query['id'],
                 titulo=query['title'],
                 descripcion=query['overview'],
                 portada="https://image.tmdb.org/t/p/w500/" +
                 query['poster_path'],
                 fecha=query['release_date'],
                 video=get_video(id_))
    return peli


def get_video(id_: str) -> Optional[str]:
    """Devuelve la direccion del trailer de youtube dado su id.
    Devuelve None si no encuentra nada.
    """
    query = (requests.get("https://api.themoviedb.org/3/movie/" +
             id_+"/videos?api_key="+api_key)).json()
    pelicula = query['results']
    if pelicula:
        for p in pelicula:
            if p['type'] == 'Trailer':
                video = p['key']
                break
    else:
        return None
    return video


def get_similar(movie_: Movie) -> List[Movie]:
    """Devuelve lista de peliculas similares dado una pelicula.
    """
    id_ = str(movie_.id)
    query = (requests.get("https://api.themoviedb.org/3/movie/"+id_ +
                          "/similar?api_key="+api_key +
                          "&language=es-ES")).json()
    pelicula = query['results']
    lista = []
    for data in pelicula:
        peli = Movie(id=data['id'],
                     titulo=data['title'],
                     descripcion=data['overview'],
                     portada="https://image.tmdb.org/t/p/original/" +
                     data['poster_path'],
                     fecha=data['release_date'])
        lista.append(peli)
    return lista


def set_genre(movie_: Movie, genres_: Iterable[dict]):
    """Setea los generos de una pelicula dado su id.
    """
    for _ in genres_:
        genre = Genero(id=_['id'], nombre=_['name'])
        movie_.generos.append(genre)


def get_in_db(movie_: Movie) -> Optional[Movie]:
    """Devuelve la instancia de la pelicula guardada en la base de dados dado
    su id.
    """
    return session.query(Movie).get(movie_.id)


def get_by_genre(genre_: Genero, pag: str) -> List[Movie]:
    """Devuelve listado de todas las peliculas dado un genero.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/discover/movie?api_key="+api_key +
        "&language=es-ES&page="+pag+"&sort_by=popularity.desc&with_genres="+str(
            genre_.id))).json()
    lista = []
    for data in query['results']:
        if data['poster_path']:
            peli = Movie(id=data['id'],
                        titulo=data['title'],
                        descripcion=data['overview'],
                        portada="https://image.tmdb.org/t/p/original/" +
                        data['poster_path'],
                        fecha=data['release_date'])
            lista.append(peli)
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
    """Devuelve lista de las peliculas en tendencias de hoy.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/trending/movie/day?api_key=" +
        api_key+"&language=es-ES")).json()
    lista = []
    for data in query['results']:
        peli = Movie(id=data['id'],
                     titulo=data['title'],
                     descripcion=data['overview'],
                     portada="https://image.tmdb.org/t/p/original/" +
                     data['poster_path'],
                     fecha=data['release_date'])
        lista.append(peli)
    return lista


def top_rated(pag: str) -> List[Movie]:
    """Devuelve lista del top de peliculas.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/movie/top_rated?api_key="+api_key +
        "&language=es-ES&page="+pag)).json()
    lista = []
    for data in query['results']:
        if data['poster_path']:
            peli = Movie(id=data['id'],
                         titulo=data['title'],
                         descripcion=data['overview'],
                         portada="https://image.tmdb.org/t/p/original/" +
                         data['poster_path'],
                         fecha=data['release_date'])
            lista.append(peli)
    return lista


def upcoming(pag: str) -> List[Movie]:
    """Devuelva listado de los proximos estrenos.
    """
    query = (requests.get("https://api.themoviedb.org/3/discover/movie?api_key="+api_key +
             "&language=es-ES&sort_by=popularity.desc&page="+pag+"&primary_release_date.gte=2021-10-10&primary_release_date.lte=2021-12-30&year=2021")).json()
    lista = []
    for data in query['results']:
        if data['poster_path']:
            peli = Movie(id=data['id'],
                         titulo=data['title'],
                         descripcion=data['overview'],
                         portada="https://image.tmdb.org/t/p/original/" +
                         data['poster_path'],
                         fecha=data['release_date'])
            lista.append(peli)
    return lista
