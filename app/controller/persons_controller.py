from typing import List
from ..database import persons_db
from ..models.models import Person


def lista_popular(pag: str) -> List[Person]:
    paginas = calcula_paginas(pag)
    listado_popular = persons_db.lista_popular(pag)
    return listado_popular, paginas


def get_person(person_: Person) -> Person:
    return persons_db.get_person(person_)


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