from flask import Blueprint, render_template

from ..controller.persons_controller import lista_popular

person = Blueprint("person", __name__)


@person.route('/persons/', methods=['GET'])
def persons():
    populares = lista_popular()
    return render_template('people.html', lista=populares)
