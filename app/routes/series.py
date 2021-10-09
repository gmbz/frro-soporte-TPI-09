from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user

from ..controller.series_controller import get_details, lista_popular, lista_recomendations, lista_top_rated

series = Blueprint("series", __name__)


@series.route('/series/populares/page=<pag>', methods=['GET'])
def series_populares(pag):
    populares_lista, paginas = lista_popular(pag)
    lista_paginas, prev_pag, next_pag = paginas
    url = 'series.series_populares'
    return render_template('series_populares.html', lista=populares_lista,
                           pages=lista_paginas, prev=prev_pag, next=next_pag,
                           url=url)


@series.route('/series/<id_serie>/', methods=['GET'])
def serie_details(id_serie):
    serie = get_details(id_serie)
    recomendations = lista_recomendations(id_serie)
    return render_template('serie.html', s=serie, rec=recomendations)


@series.route('/series/top_rated/page=<pag>', methods=['GET'])
def series_top_rated(pag):
    top_rated_lista, paginas = lista_top_rated(pag)
    lista_paginas, prev_pag, next_pag = paginas
    url = 'series.series_top_rated'
    return render_template('series_populares.html', lista=top_rated_lista,
                           pages=lista_paginas, prev=prev_pag, next=next_pag,
                           url=url)
