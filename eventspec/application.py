import os
import eventspec as app_root

from flask import Flask
from eventspec.blueprints import api, home
from eventspec import views

APP_DIR = os.path.abspath(os.path.dirname(app_root.__file__))
TEMPLATES_FOLDER = os.path.join(APP_DIR, "templates")
STATIC_FOLDER = os.path.join(APP_DIR, "static")


def create_app():
    app = Flask(__name__, template_folder=TEMPLATES_FOLDER, static_folder=STATIC_FOLDER)
    app.register_blueprint(api)
    app.register_blueprint(home)
    return app

