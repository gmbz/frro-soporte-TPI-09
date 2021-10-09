from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import current_user
from flask_login.utils import login_required

from ..models.models import Genero, Movie, Comentario
from ..controller.movies_controller import popular, search_movie, movie, similiares, get_by_genre, trending_day, top_rated
from ..controller.comments_controller import lista_por_pelicula, registrar_comentario


main = Blueprint("main", __name__)


@main.route('/')
def home():
    pag = '1'
    pop, _ = popular(pag)
    trending_list_1, trending_list_2, trending_list_3, trending_list_4, = trending_day()
    top, _ = top_rated(pag)
    return render_template('index.html', lista=pop, top=top, trending1=trending_list_1,
                           trending2=trending_list_2, trending3=trending_list_3,
                           trending4=trending_list_4)


@main.route('/search/', methods=['POST'])
def search():
    pelicula = Movie(titulo=request.form['search'])
    movies = search_movie(pelicula)
    return render_template('index.html', lista=movies)


@main.route('/movie/<id_movie>', methods=['GET'])
def movie_id(id_movie):
    pelicula = Movie(id=int(id_movie))
    peli = movie(pelicula)
    similiar = similiares(pelicula)
    comentarios = lista_por_pelicula(pelicula)
    return render_template('movie.html', mov=peli, sim=similiar,
                           com=comentarios)


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
    peliculas, paginas = get_by_genre(genre_, pag)
    lista_paginas, prev_pag, next_pag = paginas
    url = 'main.genre'
    
    return render_template('genre.html', peli=peliculas, pages=lista_paginas,
                           prev=prev_pag, next=next_pag, url=url, genre_name=genre_name)
