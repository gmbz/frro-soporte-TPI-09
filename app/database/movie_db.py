from typing import List, Iterable

from sqlalchemy.sql.expression import null

from ..models.models import Genero, Movie

import requests

api_key = "25398bd0f8e1460f3769b59bfbf5eea6"  
def lista_popular() -> List[Movie]:
    query = requests.get("https://api.themoviedb.org/3/movie/popular?api_key="+api_key+"&language=es-ES")
    j = query.json()
    pelicula = j['results']
    lista = []
    for data in pelicula:
        peli = Movie(id = data['id'],
                titulo = data['title'],
                descripcion = data['overview'],
                portada = "https://image.tmdb.org/t/p/original/"+data['poster_path'],
                fecha = data['release_date'])
        lista.append(peli)
    return lista

def search(movie_: Movie) -> List[Movie]:
    query = requests.get("https://api.themoviedb.org/3/search/movie?api_key="+api_key+"&language=es-ES&query="+movie_.titulo)
    j = query.json()
    pelicula = j['results']
    lista = []
    for data in pelicula:
        if data['poster_path']:
            peli = Movie(id = data['id'],
                    titulo = data['title'],
                    descripcion = data['overview'],
                    portada = "https://image.tmdb.org/t/p/w500/"+data['poster_path'],
                    fecha = data['release_date'])
            lista.append(peli)
    return lista

def movie(movie_: Movie) -> Movie:
    id_ = str(movie_.id)
    query = (requests.get("https://api.themoviedb.org/3/movie/"+id_+"?api_key="+api_key+"&language=es-ES")).json()
    genres = query['genres']
    peli = Movie(id = query['id'],
            titulo = query['title'],
            descripcion = query['overview'],
            portada = "https://image.tmdb.org/t/p/w500/"+query['poster_path'],
            fecha = query['release_date'],
            video = get_video(id_))
    set_genre(peli, genres)
    return peli

def get_video(id_: str) -> str:
    query = (requests.get("https://api.themoviedb.org/3/movie/"+id_+"/videos?api_key="+api_key)).json()
    pelicula = query['results']
    for p in pelicula:
        if p['type']=='Trailer':
            video = p['key']
            break
    return video

def get_similar(movie_: Movie) -> List[Movie]:
    id_= str(movie_.id)
    query = (requests.get("https://api.themoviedb.org/3/movie/"+id_+"/similar?api_key="+api_key+"&language=es-ES")).json()
    pelicula = query['results']
    lista = []
    for data in pelicula:
        peli = Movie(id = data['id'],
                titulo = data['title'],
                descripcion = data['overview'],
                portada = "https://image.tmdb.org/t/p/original/"+data['poster_path'],
                fecha = data['release_date'])
        lista.append(peli)
    return lista

def set_genre(movie_: Movie, genres_: Iterable[dict]):
    for _ in genres_:
        genre = Genero(id=_['id'], nombre=_['name'])
        movie_.generos.append(genre)