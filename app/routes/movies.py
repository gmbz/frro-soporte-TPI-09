from flask import Blueprint, render_template
from flask_login import current_user

from ..models.models import Movie, Usuario

from ..controller.listas_controller import listado_por_usuario
from ..controller.comments_controller import lista_por_pelicula
from ..helpers.helper import calcula_paginas
from ..controller import movies_controller

movies = Blueprint("movies", __name__)


@movies.route('/movie/<id_movie>', methods=['GET'])
def movie_id(id_movie):
    pelicula = Movie(id=int(id_movie))
    peli = movies_controller.movie(pelicula)
    rec = movies_controller.get_recommendations(pelicula)
    comentarios = lista_por_pelicula(pelicula)
    reparto = movies_controller.get_movie_credits(pelicula)
    title = "Película"
    if not current_user.is_anonymous:
        # SI EL USUARIO ESTA LOGUEADO, SE ENVIA LA LISTA DE "MIS LISTAS"
        id_user = current_user.id
        user = Usuario(id=id_user)
        listas_del_usuario = listado_por_usuario(user)
        return render_template('movie.html', mov=peli, lista=rec,
                               com=comentarios, listas=listas_del_usuario,
                               reparto=reparto, title=title)
    # SI NO ESTA LOGUEADO SE RENDERIZA EL HTML NORMALMENTE
    return render_template('movie.html', mov=peli, lista=rec,
                           com=comentarios, reparto=reparto, title=title)


@movies.route('/movies/populares/page=<pag>', methods=['GET'])
def movies_populares(pag):
    populares_lista = movies_controller.popular(pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'movies.movies_populares'
    title = "Películas populares"
    return render_template('populares.html', lista=populares_lista,
                           pages=lista_paginas, prev=prev_pag,
                           next=next_pag, url=url, title=title)


@movies.route('/movies/top_rated/page=<pag>', methods=['GET'])
def movies_top_rated(pag):
    top_rated_lista = movies_controller.top_rated(pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'movies.movies_top_rated'
    title = "Películas más valoradas"
    return render_template('populares.html', lista=top_rated_lista,
                           pages=lista_paginas, prev=prev_pag,
                           next=next_pag, url=url, title=title)


@movies.route('/movies/upcoming/page=<pag>', methods=['GET'])
def movies_upcoming(pag):
    upcoming_lista = movies_controller.upcoming(pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'movies.movies_upcoming'
    title = "Próximas películas"
    return render_template('populares.html', lista=upcoming_lista,
                           pages=lista_paginas, prev=prev_pag,
                           next=next_pag, url=url, title=title)
