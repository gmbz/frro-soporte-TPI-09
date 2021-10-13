import datetime
from typing import List, Optional
import requests

from ..models.models import Serie
from .db import session

api_key = '25398bd0f8e1460f3769b59bfbf5eea6'


def lista_popular(pag: str) -> List[Serie]:
    """Devuelve listado de series populares.
    """
    query = (requests.get("https://api.themoviedb.org/3/tv/popular?api_key=" +
             api_key+"&language=es-ES&page="+pag)).json()
    lista = []
    for data in query['results']:
        if data['poster_path']:
            serie = Serie(id=data['id'], nombre=data['name'],
                          descripcion=data['overview'],
                          portada="https://image.tmdb.org/t/p/original/" +
                          data['poster_path'],
                          fecha_date=datetime.datetime.strptime(
                              data['first_air_date'], "%Y-%m-%d")
                          )
            set_fecha(serie)
            lista.append(serie)
    return lista


def details(id_serie: str) -> Serie:
    """Devuelve la instancia de la serie dado su id.
    """
    query = (requests.get("https://api.themoviedb.org/3/tv/" +
             id_serie+"?api_key="+api_key+"&language=es-ES")).json()
    serie = Serie(id=query['id'], nombre=query['name'],
                  descripcion=query['overview'],
                  portada="https://image.tmdb.org/t/p/original/" +
                  query['poster_path'],
                  fecha_date=datetime.datetime.strptime(
                      query['first_air_date'], "%Y-%m-%d"),
                  video=get_video(id_serie))
    set_fecha(serie)
    return serie


def get_video(id_serie: str) -> Optional[str]:
    """Devuelve la direccion del trailer de youtube dado su id.
    Devuelve None si no encuentra nada.
    """
    query = (requests.get("https://api.themoviedb.org/3/tv/" +
             id_serie+"/videos?api_key="+api_key)).json()
    serie = query['results']
    if serie:
        for s in serie:
            if s['type'] == 'Trailer':
                video = s['key']
                break
    else:
        return None
    return video


def lista_top_rated(pag: str) -> List[Serie]:
    """Devuelve listado de series mas valoradas.
    """
    query = (requests.get("https://api.themoviedb.org/3/tv/top_rated?api_key=" +
             api_key+"&language=es-ES&page="+pag)).json()
    lista = []
    for data in query['results']:
        if data['poster_path']:
            serie = Serie(id=data['id'], nombre=data['name'],
                          descripcion=data['overview'],
                          portada="https://image.tmdb.org/t/p/original/" +
                          data['poster_path'],
                          fecha_date=datetime.datetime.strptime(
                              data['first_air_date'], "%Y-%m-%d")
                          )
            set_fecha(serie)
            lista.append(serie)
    return lista


def lista_recomendations(id_serie: str) -> List[Serie]:
    """Devuelve listado de series recomendadas dado un id.
    """
    query = (requests.get("https://api.themoviedb.org/3/tv/"+id_serie +
             "/recommendations?api_key="+api_key+"&language=es-ES")).json()
    lista = []
    for data in query['results']:
        if data['poster_path']:
            serie = Serie(id=data['id'], nombre=data['name'],
                          descripcion=data['overview'],
                          portada="https://image.tmdb.org/t/p/original/" +
                          data['poster_path'],
                          fecha_date=datetime.datetime.strptime(
                              data['first_air_date'], "%Y-%m-%d")
                          )
            set_fecha(serie)
            lista.append(serie)
    return lista


def get_in_db(serie_: Serie) -> Optional[Serie]:
    """Devuelve la instancia de la serie guardada en la base de dados dado
    su id.
    """
    return session.query(Serie).get(serie_.id)


def set_fecha(serie: Serie) -> None:
    """
    Setea la fecha que se mostrará en la web.
    """
    serie.fecha_string = serie.fecha_date.strftime("%d %b %Y")