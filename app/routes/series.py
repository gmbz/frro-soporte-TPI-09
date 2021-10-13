from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user

from ..models.models import Usuario
from ..controller.series_controller import get_details, lista_popular, lista_recomendations, lista_top_rated
from ..controller.listas_controller import listado_por_usuario

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
    if not current_user.is_anonymous:
        # SI EL USUARIO ESTA LOGUEADO, SE ENVIA LA LISTA DE "MIS LISTAS"
        id_user = current_user.id
        user = Usuario(id=id_user)
        listas_del_usuario = listado_por_usuario(user)
        return render_template('serie.html', s=serie, lista=recomendations,
                               listas=listas_del_usuario)
    # SI NO ESTA LOGUEADO SE RENDERIZA EL HTML NORMALMENTE
    return render_template('serie.html', s=serie, lista=recomendations)


@series.route('/series/top_rated/page=<pag>', methods=['GET'])
def series_top_rated(pag):
    top_rated_lista, paginas = lista_top_rated(pag)
    lista_paginas, prev_pag, next_pag = paginas
    url = 'series.series_top_rated'
    return render_template('series_populares.html', lista=top_rated_lista,
                           pages=lista_paginas, prev=prev_pag, next=next_pag,
                           url=url)