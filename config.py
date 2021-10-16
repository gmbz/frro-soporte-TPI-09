class Config:
    DEBUG = True
    SECRET_KEY = "mysecretkey"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"

    IMAGES_DIR = "app/database/img/"

    RECAPTCHA_PUBLIC_KEY = '6Le2zdEcAAAAAP99JUb0lHKzTo0gbeEeJBP6MhTF'
    RECAPTCHA_PRIVATE_KEY = '6Le2zdEcAAAAANpsrZOm39lVRicEST8Z6dEIIfmP'
