from typing import List
from ..database import serie_db
from ..models.models import Serie


def lista_popular(pag: str) -> List[Serie]:
    paginas = calcula_paginas(pag)
    listado_populares = serie_db.lista_popular(pag)
    return listado_populares, paginas


def get_details(id_serie: str) -> Serie:
    return serie_db.details(id_serie)


def lista_top_rated(pag: str) -> List[Serie]:
    paginas = calcula_paginas(pag)
    listado_top = serie_db.lista_top_rated(pag)
    return listado_top, paginas


def lista_recomendations(id_serie: str) -> List[Serie]:
    return serie_db.lista_recomendations(id_serie)


def calcula_paginas(pag: str):
    """Calcula los numeros que se van a mostrar en la paginación.
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
