import datetime
from typing import List, Optional, Iterable
import requests

from ..models.models import Season, Serie, Person
from . import api_key


def search(serie: Serie) -> List[Serie]:
    """
    Devuelve listado de series dado nombre.
    """
    query = (requests.get("https://api.themoviedb.org/3/search/tv?api_key=" +
             api_key+"&language=es-ES&include_adult=false&query="+serie.nombre
                          )).json()
    lista = []
    set_serie_list(lista, query)
    return lista


def details(serie_: Serie) -> Serie:
    """
    Devuelve la instancia de la serie dado su id.
    """
    id_ = str(serie_.id)
    query = (requests.get("https://api.themoviedb.org/3/tv/" +
             id_+"?api_key="+api_key+"&language=es-ES")).json()
    serie = Serie(id=query['id'], nombre=query['name'],
                  descripcion=query['overview'],
                  pagina_principal=query['homepage'],
                  valoracion=int(query['vote_average']*10),
                  portada="https://image.tmdb.org/t/p/original/" +
                  query['poster_path'],
                  fecha_date=datetime.datetime.strptime(
                      query['first_air_date'], "%Y-%m-%d"),
                  video=get_video(id_))
    set_seasons(serie, query)
    set_fecha(serie)
    return serie


def lista_popular(pag: str) -> List[Serie]:
    """
    Devuelve listado de series populares.
    """
    query = (requests.get("https://api.themoviedb.org/3/tv/popular?api_key=" +
             api_key+"&language=es-ES&page="+pag)).json()
    lista = []
    set_serie_list(lista, query)
    return lista


def lista_top_rated(pag: str) -> List[Serie]:
    """
    Devuelve listado de series mas valoradas.
    """
    query = (requests.get(
        "https://api.themoviedb.org/3/tv/top_rated?api_key=" +
             api_key+"&language=es-ES&page="+pag)).json()
    lista = []
    set_serie_list(lista, query)
    return lista


def lista_recomendations(serie_: Serie) -> List[Serie]:
    """
    Devuelve listado de series recomendadas dado un id.
    """
    query = (requests.get("https://api.themoviedb.org/3/tv/"+str(serie_.id) +
             "/recommendations?api_key="+api_key+"&language=es-ES")).json()
    lista = []
    set_serie_list(lista, query)
    return lista


def serie_credits(serie_: Serie) -> List[Serie]:
    """
    Devuelve listado del reparto de la pelicula.
    """
    query = (requests.get("https://api.themoviedb.org/3/tv/" +
             str(serie_.id)+"/credits?api_key="+api_key+"&language=es-ES")
             ).json()
    lista = []
    for data in query['cast']:
        if data['profile_path']:
            per = Person(id=data['id'],
                         nombre=data['name'],
                         perfil="https://image.tmdb.org/t/p/original/" +
                         data['profile_path'])
            lista.append(per)
    return lista


def set_fecha(serie: Serie) -> None:
    """
    Setea la fecha que se mostrará en la web.
    """
    serie.fecha_string = serie.fecha_date.strftime("%d %b %Y")


def set_seasons(serie: Serie, query) -> None:
    """
    Setea las temporadas de la serie dada.
    """
    for data in query['seasons']:
        season = Season(id=data['id'],
                        episodios=data['episode_count'],
                        nombre=data['name'],
                        numero=data['season_number'])
        if data['poster_path']:
            season.portada = "https://image.tmdb.org/t/p/original/" + \
                data['poster_path']
        serie.seasons.append(season)


def set_serie_list(lista: Iterable, query) -> None:
    """
    Setea los datos de la lista.
    """
    try:
        for data in query['results']:
            if data['poster_path']:
                if data['first_air_date']:
                    serie = Serie(id=data['id'],
                                  nombre=data['name'],
                                  descripcion=data['overview'],
                                  valoracion=int(data['vote_average']*10),
                                  portada="https://image.tmdb.org/t/p/original/" +
                                  data['poster_path'],
                                  fecha_date=datetime.datetime.strptime(
                        data['first_air_date'], "%Y-%m-%d"))
                    set_fecha(serie)
                    lista.append(serie)
    except:
        return None


def get_video(id_serie: str) -> Optional[str]:
    """
    Devuelve la direccion del trailer de youtube dado su id.
    Devuelve None si no encuentra nada.
    """
    try:
        query = (requests.get("https://api.themoviedb.org/3/tv/" +
                              id_serie+"/videos?api_key="+api_key)).json()
        if query['results']:
            for data in query['results']:
                if data['type'] == 'Trailer':
                    video = data['key']
                    break
        return video
    except:
        return None
