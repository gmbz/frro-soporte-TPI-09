from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField

class RegistroUsuario(Form):
    username = StringField('username')
    password = PasswordField('password')
    email = EmailField('Email')
    submit = SubmitField('Registrar')

class Login(Form):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('Login')