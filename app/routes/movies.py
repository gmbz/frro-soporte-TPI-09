from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user

from ..controller.movies_controller import popular, top_rated, upcoming

movies = Blueprint("movies", __name__)


@movies.route('/movies/populares/page=<pag>', methods=['GET'])
def movies_populares(pag):
    populares_lista, paginas = popular(pag)
    lista_paginas, prev_pag, next_pag = paginas
    url = 'movies.movies_populares'
    return render_template('populares.html', lista=populares_lista,
                           pages=lista_paginas, prev=prev_pag,
                           next=next_pag, url=url)


@movies.route('/movies/top_rated/page=<pag>', methods=['GET'])
def movies_top_rated(pag):
    top_rated_lista, paginas = top_rated(pag)
    lista_paginas, prev_pag, next_pag = paginas
    url = 'movies.movies_top_rated'
    return render_template('populares.html', lista=top_rated_lista,
                           pages=lista_paginas, prev=prev_pag,
                           next=next_pag, url=url)


@movies.route('/movies/upcoming/page=<pag>', methods=['GET'])
def movies_upcoming(pag):
    upcoming_lista, paginas = upcoming(pag)
    lista_paginas, prev_pag, next_pag = paginas
    url = 'movies.movies_upcoming'
    return render_template('populares.html', lista=upcoming_lista,
                           pages=lista_paginas, prev=prev_pag,
                           next=next_pag, url=url)
