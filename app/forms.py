from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea
from flask_wtf import RecaptchaField


class RegistroUsuario(Form):
    username = StringField('Nombre de usuario', validators=[
                           DataRequired(), Length(max=30)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Registrar')


class Login(Form):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Login')


class NuevaLista(Form):
    nombre = StringField('Nombre de lista', validators=[
                         DataRequired(), Length(max=32)])
    submit = SubmitField('Crear')


class Comentario(Form):
    contenido = StringField('Texto', widget=TextArea(), validators=[
                            DataRequired(), Length(max=255)])


class ChangePass(Form):
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Cambiar contraseña')
