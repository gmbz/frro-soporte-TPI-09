from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from flask_login import LoginManager, login_user, current_user, logout_user
from flask_login.utils import login_required

from .models.models import Comentario, Movie, Usuario
from .forms import RegistroUsuario, Login
from .controller.users_controller import register_user, autenticacion, buscar_id
from .controller.movies_controller import popular, search_movie, movie, similiares
from .controller.comments_controller import lista_por_pelicula, registrar_comentario

app = Flask(__name__, template_folder="views/templates/",
            static_folder="views/static/")
app.secret_key = "mysecretkey"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(id):
    return buscar_id(int(id))

# modificar


@app.route('/')
def home():
    pop = popular()
    return render_template('index.html', lista=pop)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    register_form = RegistroUsuario(request.form)
    if request.method == 'POST':
        user_ = Usuario(username=register_form.username.data,
                        password=register_form.password.data,
                        email=register_form.email.data)
        user = register_user(user_)
        print(user.username)
        flash(f"Usuario {user.username} registrado")
        return redirect(url_for('register'))
    return render_template('register.html', form=register_form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = Login(request.form)
    if request.method == 'POST':
        username_ = login_form.username.data
        password_ = login_form.password.data
        user_ = autenticacion(username_, password_)
        prueba = login_user(user_)
        print("-------------------------------------")
        print(current_user.username)
        print(prueba)
        print("-------------------------------------")
        if user_:
            flash(f"Logueado {current_user.username}")
        return redirect(url_for('login'))
    return render_template('login.html', form=login_form)

@app.route('/search/', methods = ['POST'])
def search():
    pelicula = Movie(titulo = request.form['search'])
    movies = search_movie(pelicula)
    return render_template('index.html', lista=movies)

@app.route('/movie/<id_movie>', methods = ['GET'])
def movie_id(id_movie):
    pelicula = Movie(id = int(id_movie))
    peli = movie(pelicula)
    similiar = similiares(pelicula)
    comentarios = lista_por_pelicula(pelicula)
    return render_template('movie.html', mov=peli, sim=similiar, com=comentarios)

@app.route('/comment/', methods = ['POST'])
@login_required
def movie_comment():
    _comment = Comentario(comentario = request.form['comentario'])
    registrar_comentario(_comment)
    return redirect(url_for('movie_id'))

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
