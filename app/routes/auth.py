from flask import Blueprint, request, flash, redirect, url_for, render_template, current_app
from flask_login import login_user, current_user, logout_user
from flask_login.utils import login_required

from ..helpers import helper
from ..models.models import Usuario
from ..forms import ChangePass, RegistroUsuario, Login
from ..controller.users_controller import register_user, autenticacion
from ..controller import users_controller

auth = Blueprint("auth", __name__)


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    register_form = RegistroUsuario(request.form)
    title = "Registro"
    if request.method == 'POST':
        nombre_image = "icons8-user-64.png"
        user_ = Usuario(username=register_form.username.data,
                        password=register_form.password.data,
                        image=nombre_image,
                        email=register_form.email.data)
        captcha = request.form['g-recaptcha-response']
        if helper.is_human(captcha, current_app):
            status = "Successfully"
            user = register_user(user_)
            if isinstance(user, Usuario):
                flash(f"Usuario {user.username} registrado", 'success')
            else:
                msg = f"{user}"
                flash(msg, 'danger')
            return redirect(url_for('auth.register'))
        else:
            status = "Por favor validar que no eres un robot."
            flash(status, 'danger')
        return redirect(url_for('auth.register'))
    return render_template('register.html', form=register_form, title=title)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = Login(request.form)
    title = "Iniciar sesión"
    if request.method == 'POST':
        username_ = login_form.username.data
        password_ = login_form.password.data
        user = autenticacion(username_, password_)
        if isinstance(user, Usuario):
            login_user(user)
            flash(f"Logueado {current_user.username}", 'success')
            return redirect(url_for('auth.login'))
        msg = f"{user}"
        flash(msg, 'danger')
        return redirect(url_for('auth.login'))
    return render_template('login.html', form=login_form, title=title)


@auth.route('/change_pass/', methods=['GET', 'POST'])
@login_required
def change_pass():
    pass_form = ChangePass(request.form)
    if request.method == 'POST':
        password = pass_form.password.data
        user = Usuario(id=current_user.id, password=password)
        changed = users_controller.change_pass(user)
        if isinstance(changed, Usuario):
            logout_user()
            flash("Contraseña cambiada", 'success')
            return redirect(url_for('auth.login'))
        msg = f"{changed}"
        flash(msg, 'danger')
        return redirect(url_for('perfil.main'))
    return redirect(url_for('perfil.main'))


@auth.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
