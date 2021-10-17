import os

from flask import Blueprint, request, redirect, url_for, render_template, send_from_directory
from flask.globals import current_app
from flask_login import current_user
from flask_login.utils import login_required

from ..models.models import Genero, Movie, Comentario, Person, Serie, Usuario
from ..controller.movies_controller import get_movie_credits, popular, search_movie, movie, get_by_genre, trending_day, top_rated, get_recommendations
from ..controller.comments_controller import lista_por_pelicula, registrar_comentario
from ..controller.listas_controller import listado_por_usuario
from ..controller.persons_controller import search_person
from ..controller import series_controller

from ..helpers.helper import calcula_paginas

main = Blueprint("main", __name__)


@main.route('/')
def home():
    pop = popular()
    trending_list = trending_day()
    top = top_rated()
    series_pop = series_controller.lista_popular()
    series_top = series_controller.lista_top_rated()
    title = "Inicio"
    return render_template('index.html', lista=pop, top=top,
                           trending=trending_list, series_pop=series_pop,
                           series_top=series_top, title=title)


@main.route('/search/', methods=['POST'])
def search():
    pelicula = Movie(titulo=request.form['search'])
    serie = Serie(nombre=request.form['search'])
    persona = Person(nombre=request.form['search'])
    movies = search_movie(pelicula)
    series = series_controller.search_serie(serie)
    persons = search_person(persona)
    title = "Búsqueda"
    return render_template('search.html', movies=movies, series=series,
                           persons=persons, title=title)


@main.route('/movie/<id_movie>', methods=['GET'])
def movie_id(id_movie):
    pelicula = Movie(id=int(id_movie))
    peli = movie(pelicula)
    rec = get_recommendations(pelicula)
    comentarios = lista_por_pelicula(pelicula)
    reparto = get_movie_credits(pelicula)
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


@main.route('/comment/', methods=['POST'])
@login_required
def movie_comment():
    _movie = Movie(id=request.form['IdMovie'])
    _id_user = int(current_user.id)
    _comment = Comentario(contenido=request.form['comentario'])
    registrar_comentario(_comment, _movie, _id_user)
    return redirect(url_for('main.home'))


@main.route('/genre/<genre_name>/page=<pag>', methods=['GET'])
def genre(genre_name, pag):
    genre_ = Genero(nombre=genre_name)
    peliculas = get_by_genre(genre_, pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'main.genre'
    title = genre_.nombre
    return render_template('genre.html', lista=peliculas, pages=lista_paginas,
                           prev=prev_pag, next=next_pag, url=url,
                           genre_name=genre_name, title=title)


@main.route('/media/posts/<filename>')
def image_user(filename):
    dir_path = os.path.join(current_app.config['IMAGES_DIR'])
    return send_from_directory(dir_path, filename)
