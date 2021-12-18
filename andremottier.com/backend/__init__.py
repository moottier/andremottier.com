import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .util import SecretGetter
from .config import AppConfigBuilder
import sys

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
if __file__.find('dev') > -1:
    app_root = r'/var/www/dev.andremottier.com/andremottier.com/backend/'
else:
    app_root = r'/var/www/andremottier.com/andremottier.com/backend/'

def create_app():
    app = Flask(__name__)
    
    config = AppConfigBuilder(
        app, 
        os.path.join(app_root, 'conf.yaml'),
        os.path.join(app_root, 'secrets.yaml')
    )
    config.setFlaskConfig()
    
    print("Setting trim blocks", file=sys.stdout)
    app.jinja_options["trim_blocks"] = True
    print("Setting lstrip blocks", file=sys.stdout)
    app.jinja_options["lstrip_blocks"] = True
    print("done setting", file=sys.stdout)

#    print("getting jinja settings from __init__", file=sys.stdout)
#    print("trim_blocks: ", app.jinja_env.trim_blocks, file=sys.stdout)
#    print("lstrip_blocks: ", app.jinja_env.lstrip_blocks, file=sys.stdout)

#    print("trim_blocks: ")#, app.jinja_env.trim_blocks, file=sys.stdout)
#    print("lstrip_blocks: ")#, app.jinja_env.lstrip_blocks, file=sys.stdout)


    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for non-auth parts of app
    from .main import chat_server_php as chat_server_php_blueprint
    app.register_blueprint(chat_server_php_blueprint)

    return app
