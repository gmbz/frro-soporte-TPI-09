from typing import List

from ..models.models import Serie, Person
from . import serie_api


def lista_popular(pag: str = "1") -> List[Serie]:
    listado_populares = serie_api.lista_popular(pag)
    return listado_populares


def get_details(serie: Serie) -> Serie:
    return serie_api.details(serie)


def lista_top_rated(pag: str = "1") -> List[Serie]:
    listado_top = serie_api.lista_top_rated(pag)
    return listado_top


def lista_recomendations(serie: Serie) -> List[Serie]:
    return serie_api.lista_recomendations(serie)


def get_serie_credits(serie_: Serie) -> List[Person]:
    return serie_api.serie_credits(serie_)


def search_serie(serie: Serie) -> List[Person]:
    return serie_api.search(serie)
