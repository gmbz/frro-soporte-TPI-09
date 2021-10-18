from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user
from flask_login.utils import login_required

from ..models.models import Genero, Movie, Comentario, Person, Serie, Usuario
from ..controller.listas_controller import listado_por_usuario
from ..controller.persons_controller import search_person
from ..controller import series_controller
from ..controller import movies_controller
from ..controller import comments_controller

from ..helpers.helper import calcula_paginas

main = Blueprint("main", __name__)


@main.route('/')
def home():
    pop = movies_controller.popular()
    trending_list = movies_controller.trending_day()
    top = movies_controller.top_rated()
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
    movies = movies_controller.search_movie(pelicula)
    series = series_controller.search_serie(serie)
    persons = search_person(persona)
    title = "Búsqueda"
    return render_template('search.html', movies=movies, series=series,
                           persons=persons, title=title)


@main.route('/comment/', methods=['POST'])
@login_required
def movie_comment():
    _movie = Movie(id=request.form['IdMovie'])
    _id_user = int(current_user.id)
    _comment = Comentario(contenido=request.form['comentario'])
    comments_controller.registrar_comentario(_comment, _movie, _id_user)
    return redirect(url_for('main.home'))


@main.route('/genre/<genre_name>/page=<pag>', methods=['GET'])
def genre(genre_name, pag):
    genre_ = Genero(nombre=genre_name)
    peliculas = movies_controller.get_by_genre(genre_, pag)
    lista_paginas, prev_pag, next_pag = calcula_paginas(pag)
    url = 'main.genre'
    title = genre_.nombre
    return render_template('genre.html', lista=peliculas, pages=lista_paginas,
                           prev=prev_pag, next=next_pag, url=url,
                           genre_name=genre_name, title=title)
