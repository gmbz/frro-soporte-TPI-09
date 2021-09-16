from flask import Flask
from config import Config
from flask_login import LoginManager

from .controller.users_controller import buscar_id
from .routes import auth, main, person

app = Flask(__name__, static_folder=Config.STATIC_FOLDER,
            template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

app.register_blueprint(auth, url_prefix="/")
app.register_blueprint(main, url_prefix="/")
app.register_blueprint(person, url_prefix="/")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(id):
    return buscar_id(int(id))
