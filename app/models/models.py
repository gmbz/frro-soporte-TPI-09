from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date
from werkzeug.security import generate_password_hash, check_password_hash
Base = declarative_base()


class Usuario(Base, UserMixin):

    __tablename__ = 'usuario'
    id = Column(Integer, primary_key = True, autoincrement = True)
    username = Column(String(250), unique = True)
    password = Column(String(250))
    email = Column(String(250))

    comments = relationship("Comentario", backref='user')

    def __init__(self, username, password, email):
        self.username = username
        self.password = self.__set_password(password)
        self.email = email

    def __set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)
    
    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)
    

class Movie(Base):
    __tablename__ = 'pelicula'
    id = Column(Integer, primary_key = True)
    titulo = Column(String(250), unique = True)
    descripcion = Column(String(500))
    portada = Column(String(250))
    fecha = Column(Date)
    video = Column(String(250))

    comments = relationship("Comentario", backref='movie')
    generos = relationship("Genero", secondary = "genre_movie", back_populates = "peliculas")

class Genero(Base):
    __tablename__ = 'genero'
    
    id = Column(Integer, primary_key = True)
    nombre = Column(String(255))
    
    peliculas = relationship("Movie", secondary = "genre_movie", back_populates = "generos")

class GenreMovie(Base):
    __tablename__ = 'genre_movie'
    
    id_movie = Column(Integer, ForeignKey('pelicula.id'), primary_key=True)
    id_genero = Column(Integer, ForeignKey('genero.id'), primary_key=True)
    
    pelicula = relationship("Movie", backref = "genre_movie")
    genero = relationship("Genero", backref = "genre_movie")

class Comentario(Base):
    __tablename__ = 'comentario'

    id = Column(Integer, primary_key = True)
    contenido = Column(String(250))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_pelicula = Column(Integer, ForeignKey('pelicula.id'))