from app.models.models import Person
from flask import Blueprint, render_template

from ..controller.persons_controller import lista_popular, get_person
from ..helpers.helper import calcula_paginas

person = Blueprint("person", __name__)


@person.route('/persons/page=<pag>', methods=['GET'])
def persons(pag):
    populares = lista_popular(pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'person.persons'
    return render_template('people.html', lista=populares,
                           pages=lista_paginas, prev=prev_pag,
                           next=next_pag, url=url)


@person.route('/persons/<id_person>', methods=['GET'])
def person_id(id_person):
    _persona = Person(id=id_person)
    persona = get_person(_persona)
    return render_template('person.html', p=persona)
