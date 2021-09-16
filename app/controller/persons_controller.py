from typing import List
from ..database import persons_db
from ..models.models import Person


def lista_popular() -> List[Person]:
    return persons_db.lista_popular()
