from flask import Blueprint, render_template

from ..controller.movies_controller import popular, top_rated, upcoming
from ..helpers.helper import calcula_paginas

movies = Blueprint("movies", __name__)


@movies.route('/movies/populares/page=<pag>', methods=['GET'])
def movies_populares(pag):
    populares_lista = popular(pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'movies.movies_populares'
    title = "Películas populares"
    return render_template('populares.html', lista=populares_lista,
                           pages=lista_paginas, prev=prev_pag,
                           next=next_pag, url=url, title=title)


@movies.route('/movies/top_rated/page=<pag>', methods=['GET'])
def movies_top_rated(pag):
    top_rated_lista = top_rated(pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'movies.movies_top_rated'
    title = "Películas más valoradas"
    return render_template('populares.html', lista=top_rated_lista,
                           pages=lista_paginas, prev=prev_pag,
                           next=next_pag, url=url, title=title)


@movies.route('/movies/upcoming/page=<pag>', methods=['GET'])
def movies_upcoming(pag):
    upcoming_lista = upcoming(pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'movies.movies_upcoming'
    title = "Próximas películas"
    return render_template('populares.html', lista=upcoming_lista,
                           pages=lista_paginas, prev=prev_pag,
                           next=next_pag, url=url, title=title)
