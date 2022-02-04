import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from andremottier.util import SecretGetter
from andremottier.config import Config
import sys

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app(config_class=Config):    # TODO: make Config default arg
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from andremottier.backend.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))


    from andremottier.backend.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from andremottier.backend.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # TODO: necessary to register project blueprints if not visiting projects endpoint?
    from andremottier.projects.routes import projects as projects_blueprint
    app.register_blueprint(projects_blueprint)

    return app
