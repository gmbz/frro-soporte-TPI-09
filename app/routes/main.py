from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_user, current_user, logout_user
from flask_login.utils import login_required

from ..models.models import Usuario, Movie, Comentario
from ..controller.users_controller import register_user, autenticacion
from ..controller.movies_controller import popular, search_movie, movie, similiares
from ..controller.comments_controller import lista_por_pelicula, registrar_comentario


main = Blueprint("main", __name__)

@main.route('/')
def home():
    pop = popular()
    return render_template('index.html', lista=pop)



@main.route('/search/', methods = ['POST'])
def search():
    pelicula = Movie(titulo = request.form['search'])
    movies = search_movie(pelicula)
    return render_template('index.html', lista=movies)

@main.route('/movie/<id_movie>', methods = ['GET'])
def movie_id(id_movie):
    pelicula = Movie(id = int(id_movie))
    peli = movie(pelicula)
    similiar = similiares(pelicula)
    comentarios = lista_por_pelicula(pelicula)
    return render_template('movie.html', mov=peli, sim=similiar, com=comentarios)

@main.route('/comment/', methods = ['POST'])
@login_required
def movie_comment():
    _movie = Movie(id=request.form['IdMovie'])
    _user = Usuario(id=current_user.id)
    _comment = Comentario(contenido=request.form['comentario'])
    registrar_comentario(_comment, _movie, _user)
    return redirect(url_for('main.home'))
