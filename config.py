import os


class Config:
    DEBUG = False
    SECRET_KEY = "mysecretkey"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"
