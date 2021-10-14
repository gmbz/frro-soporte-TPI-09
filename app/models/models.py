from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DATE, DATETIME
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()


class Usuario(Base, UserMixin):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(250), unique=True)
    password = Column(String(250))
    email = Column(String(250))

    comments = relationship("Comentario", backref='user')
    listas = relationship("MisListas", backref='user')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)


class Movie(Base):
    __tablename__ = 'pelicula'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), unique=True)
    descripcion = Column(String(500))
    portada = Column(String(250))
    fecha_date = Column(DATE)
    fecha_string = Column(String(250))
    video = Column(String(250))

    comments = relationship("Comentario", backref='movie')
    generos = relationship(
        "Genero", secondary="genre_movie", back_populates="peliculas")
    personas = relationship("Person", secondary="person_movie",
                            back_populates="peliculas")
    listas = relationship("MisListas")


class Genero(Base):
    __tablename__ = 'genero'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))

    peliculas = relationship(
        "Movie", secondary="genre_movie", back_populates="generos")


class GenreMovie(Base):
    __tablename__ = 'genre_movie'

    id_movie = Column(Integer, ForeignKey('pelicula.id'), primary_key=True)
    id_genero = Column(Integer, ForeignKey('genero.id'), primary_key=True)

    pelicula = relationship("Movie", backref="genre_movie")
    genero = relationship("Genero", backref="genre_movie")


class Comentario(Base):
    __tablename__ = 'comentario'

    id = Column(Integer, primary_key=True)
    contenido = Column(String(250))
    fecha = Column(DATETIME)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_pelicula = Column(Integer, ForeignKey('pelicula.id'))
    id_serie = Column(Integer, ForeignKey('serie.id'))


class Person(Base):
    __tablename__ = 'persona'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    perfil = Column(String(255))
    fecha_nacimiento = Column(String(255))
    biografia = Column(String(255))

    peliculas = relationship("Movie", secondary="person_movie",
                             back_populates="personas")


class PersonMovie(Base):
    __tablename__ = 'person_movie'

    id_person = Column(Integer, ForeignKey('persona.id'), primary_key=True)
    id_movie = Column(Integer, ForeignKey('pelicula.id'), primary_key=True)

    persona = relationship("Person", backref="person_movie")
    pelicula = relationship("Movie", backref="person_movie")


class PersonSerie(Base):
    __tablename__ = 'person_serie'

    id_person = Column(Integer, ForeignKey('persona.id'), primary_key=True)
    id_serie = Column(Integer, ForeignKey('serie.id'), primary_key=True)

    persona = relationship("Person", backref="person_serie")
    pelicula = relationship("Serie", backref="person_serie")


class Serie(Base):
    __tablename__ = 'serie'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    descripcion = Column(String(500))
    fecha_date = Column(DATE)
    fecha_string = Column(String(250))
    portada = Column(String(250))
    video = Column(String(250))

    listas = relationship("MisListas")
    comments = relationship("Comentario", backref='serie')


class MisListas(Base):
    __tablename__ = 'mis_listas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    id_user = Column(Integer, ForeignKey('usuario.id'))
    id_movie = Column(Integer, ForeignKey('pelicula.id'))
    id_serie = Column(Integer, ForeignKey('serie.id'))

    peliculas = relationship("Movie", secondary='mis_listas_movie')
    series = relationship("Serie", secondary='mis_listas_serie')


class MisListasMovie(Base):
    __tablename__ = 'mis_listas_movie'

    id_lista = Column(Integer, ForeignKey('mis_listas.id'), primary_key=True)
    id_movie = Column(Integer, ForeignKey('pelicula.id'), primary_key=True)

    lista = relationship("MisListas", backref="mis_listas_movie")
    pelicula = relationship("Movie", backref="mis_listas_movie")


class MisListasSerie(Base):
    __tablename__ = 'mis_listas_serie'

    id_lista = Column(Integer, ForeignKey('mis_listas.id'), primary_key=True)
    id_serie = Column(Integer, ForeignKey('serie.id'), primary_key=True)

    lista = relationship("MisListas", backref="mis_listas_serie")
    serie = relationship("Serie", backref="mis_listas_serie")
