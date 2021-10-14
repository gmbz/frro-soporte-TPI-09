from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField


class RegistroUsuario(Form):
    username = StringField('Nombre de usuario')
    password = PasswordField('Contraseña')
    email = EmailField('Email')
    submit = SubmitField('Registrar')


class Login(Form):
    username = StringField('Nombre de usuario')
    password = PasswordField('Contraseña')
    submit = SubmitField('Login')


class NuevaLista(Form):
    nombre = StringField('Nombre de lista')
    submit = SubmitField('Crear')
