from flask import Blueprint, request, redirect, url_for, render_template
from flask.helpers import flash
from flask_login import current_user
from flask_login.utils import login_required

from ..forms import ChangePass, NuevaLista
from ..models.models import MisListas, Movie, Serie, Usuario
from ..controller.listas_controller import add_movie, add_serie, get_list, listado_por_usuario, crear_lista, borrar_lista
from ..controller import listas_controller

perfil = Blueprint("perfil", __name__)


@perfil.route('/show_list/<id_lista>', methods=['GET', 'POST'])
@perfil.route('/', methods=['GET', 'POST'])
@login_required
def main(id_lista=""):
    form = NuevaLista(request.form)
    form_change = ChangePass(request.form)
    id_user = current_user.id
    user = Usuario(id=id_user)
    listado_mis_listas = listado_por_usuario(user)
    title = "Perfil"
    # SI RECIBE UNA LISTA PARA VISUALIZAR, SE BUSCA Y SE RENDERIZA CON EL CONTENIDO DE LA LISTA
    if id_lista:
        mi_lista_ = MisListas(id=id_lista)
        mi_lista = get_list(mi_lista_)
        return render_template('perfil.html', mis_listas=listado_mis_listas,
                               form=form, form_change=form_change,
                               mi_lista=mi_lista, title=title)
    # SI NO RECIBE UNA LISTA, MUESTRA EL CONTENIDO NORMALMENTE
    return render_template('perfil.html', mis_listas=listado_mis_listas,
                           form=form, form_change=form_change, title=title)


@perfil.route('/nueva_lista/', methods=['GET', 'POST'])
@login_required
def nueva_lista():
    form = NuevaLista(request.form)
    new_list = MisListas(nombre=form.nombre.data)
    id_user = current_user.id
    user = Usuario(id=id_user)
    mi_lista = crear_lista(new_list, user)
    flash(f"Lista {mi_lista.nombre} creada", 'success')
    return redirect(url_for('perfil.main'))


@perfil.route('/borrar_lista/<id_lista>', methods=['GET', 'POST'])
@login_required
def eliminar_lista(id_lista):
    mi_lista = MisListas(id=id_lista)
    borrar_lista(mi_lista)
    flash("Lista borrada", 'success')
    return redirect(url_for('perfil.main'))


@perfil.route('/add_movie/<id_lista>/<id_movie>', methods=['GET', 'POST'])
@login_required
def add_movie_list(id_lista, id_movie):
    mi_lista_ = MisListas(id=id_lista)
    movie = Movie(id=id_movie)
    mi_lista = add_movie(mi_lista_, movie)
    flash(f"Pelicula añadida a la lista {mi_lista.nombre}", 'success')
    return redirect(url_for('movies.movie_id', id_movie=id_movie))


@perfil.route('/add_serie/<id_lista>/<id_serie>', methods=['GET', 'POST'])
@login_required
def add_serie_list(id_lista, id_serie):
    mi_lista_ = MisListas(id=id_lista)
    serie = Serie(id=id_serie)
    mi_lista = add_serie(mi_lista_, serie)
    flash(f"Serie añadida a la lista {mi_lista.nombre}", 'success')
    return redirect(url_for('series.serie_details', id_serie=id_serie))


@perfil.route('/delete_serie/<id_lista>/<id_serie>', methods=['GET', 'POST'])
@login_required
def delete_serie_list(id_lista, id_serie):
    mi_lista_ = MisListas(id=id_lista)
    serie = Serie(id=id_serie)
    mi_lista = listas_controller.borrar_serie(mi_lista_, serie)
    flash(f"Serie eliminada de la lista {mi_lista.nombre}", 'success')
    return redirect(url_for('perfil.main', id_lista=mi_lista.id))


@perfil.route('/delete_movie/<id_lista>/<id_movie>', methods=['GET', 'POST'])
@login_required
def delete_movie_list(id_lista, id_movie):
    mi_lista_ = MisListas(id=id_lista)
    movie = Serie(id=id_movie)
    mi_lista = listas_controller.borrar_movie(mi_lista_, movie)
    flash(f"Película eliminada de la lista {mi_lista.nombre}", 'success')
    return redirect(url_for('perfil.main', id_lista=mi_lista.id))
