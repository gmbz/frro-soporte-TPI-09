from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_user, current_user, logout_user

from ..models.models import Usuario
from ..forms import RegistroUsuario, Login
from ..controller.users_controller import register_user, autenticacion

auth = Blueprint("auth", __name__)


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    register_form = RegistroUsuario(request.form)
    if request.method == 'POST':
        user_ = Usuario(username=register_form.username.data,
                        password=register_form.password.data,
                        email=register_form.email.data)
        user = register_user(user_)
        if isinstance(user, Usuario):
            flash(f"Usuario {user.username} registrado", 'success')
        else:
            msg = f"{user}"
            flash(msg, 'danger')
        return redirect(url_for('auth.register'))
    return render_template('register.html', form=register_form)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = Login(request.form)
    if request.method == 'POST':
        username_ = login_form.username.data
        password_ = login_form.password.data
        user = autenticacion(username_, password_)
        if isinstance(user, Usuario):
            login_user(user)
            flash(f"Logueado {current_user.username}", 'success')
        else:
            msg = f"{user}"
            flash(msg, 'danger')
            return redirect(url_for('auth.login'))
    return render_template('login.html', form=login_form)


@auth.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
