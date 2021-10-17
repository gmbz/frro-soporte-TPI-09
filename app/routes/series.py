from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user
from flask_login.utils import login_required

from ..models.models import Usuario, Serie, Comentario
from ..controller.series_controller import (get_details, lista_popular, lista_recomendations, lista_top_rated, get_serie_credits)
from ..controller.listas_controller import listado_por_usuario
from ..controller.comments_controller import reg_comment, lista_por_serie
from ..helpers.helper import calcula_paginas

series = Blueprint("series", __name__)


@series.route('/series/populares/page=<pag>', methods=['GET'])
def series_populares(pag):
    populares_lista = lista_popular(pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'series.series_populares'
    title = "Series populares"
    return render_template('series_populares.html', lista=populares_lista,
                           pages=lista_paginas, prev=prev_pag, next=next_pag,
                           url=url, title=title)


@series.route('/series/<id_serie>/', methods=['GET'])
def serie_details(id_serie):
    serie = get_details(id_serie)
    recomendations = lista_recomendations(id_serie)
    comentarios = lista_por_serie(serie)
    reparto = get_serie_credits(serie)
    title = "Serie"
    if not current_user.is_anonymous:
        # SI EL USUARIO ESTA LOGUEADO, SE ENVIA LA LISTA DE "MIS LISTAS"
        id_user = current_user.id
        user = Usuario(id=id_user)
        listas_del_usuario = listado_por_usuario(user)
        return render_template('serie.html', s=serie, lista=recomendations,
                               listas=listas_del_usuario, com=comentarios,
                               reparto=reparto, title=title)
    # SI NO ESTA LOGUEADO SE RENDERIZA EL HTML NORMALMENTE
    return render_template('serie.html', s=serie, lista=recomendations,
                           com=comentarios, reparto=reparto, title=title)


@series.route('/series/top_rated/page=<pag>', methods=['GET'])
def series_top_rated(pag):
    top_rated_lista = lista_top_rated(pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'series.series_top_rated'
    title = "Series más valoradas"
    return render_template('series_populares.html', lista=top_rated_lista,
                           pages=lista_paginas, prev=prev_pag, next=next_pag,
                           url=url, title=title)


@series.route('/series/comment/', methods=['POST'])
@login_required
def serie_comment():
    serie = Serie(id=request.form['IdSerie'])
    id_user = int(current_user.id)
    user = Usuario(id=id_user)
    comment = Comentario(contenido=request.form['comentario'])
    reg_comment(comment, serie, user)
    return redirect(url_for('series.serie_details', id_serie=serie.id))
