from flask import Blueprint, request, redirect, url_for, render_template
from flask.helpers import flash
from flask_login import current_user
from flask_login.utils import login_required

from ..forms import NuevaLista
from ..models.models import MisListas, Movie, Serie, Usuario
from ..controller.listas_controller import add_movie, add_serie, get_list, listado_por_usuario, crear_lista, borrar_lista


perfil = Blueprint("perfil", __name__)


@perfil.route('/show_list/<id_lista>', methods=['GET', 'POST'])
@perfil.route('/', methods=['GET', 'POST'])
@login_required
def main(id_lista=""):
    form = NuevaLista(request.form)
    id_user = current_user.id
    user = Usuario(id=id_user)
    listado_mis_listas = listado_por_usuario(user)
    # SI RECIBE UNA LISTA PARA VISUALIZAR, SE BUSCA Y SE RENDERIZA CON EL CONTENIDO DE LA LISTA
    if id_lista:
        mi_lista_ = MisListas(id=id_lista)
        mi_lista = get_list(mi_lista_)
        return render_template('perfil.html', mis_listas=listado_mis_listas, form=form, mi_lista=mi_lista)
    # SI NO RECIBE UNA LISTA, MUESTRA EL CONTENIDO NORMALMENTE
    return render_template('perfil.html', mis_listas=listado_mis_listas, form=form)


@perfil.route('/nueva_lista/', methods=['GET', 'POST'])
@login_required
def nueva_lista():
    form = NuevaLista(request.form)
    new_list = MisListas(nombre=form.nombre.data)
    id_user = current_user.id
    user = Usuario(id=id_user)
    mi_lista = crear_lista(new_list, user)
    flash("Lista creada", 'success')
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
    return redirect(url_for('main.movie_id', id_movie=id_movie))


@perfil.route('/add_serie/<id_lista>/<id_serie>', methods=['GET', 'POST'])
@login_required
def add_serie_list(id_lista, id_serie):
    mi_lista_ = MisListas(id=id_lista)
    serie = Serie(id=id_serie)
    mi_lista = add_serie(mi_lista_, serie)
    flash(f"Serie añadida a la lista {mi_lista.nombre}", 'success')
    return redirect(url_for('series.serie_details', id_serie=id_serie))
