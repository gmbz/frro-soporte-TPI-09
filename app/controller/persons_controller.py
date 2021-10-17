from typing import List

from ..models.models import Person
from . import persons_api


def lista_popular(pag: str) -> List[Person]:
    listado_popular = persons_api.lista_popular(pag)
    return listado_popular


def get_person(person_: Person) -> Person:
    return persons_api.get_person(person_)


def search_person(person: Person) -> List[Person]:
    return persons_api.search(person)
