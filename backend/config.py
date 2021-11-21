from flask import Flask
from .secrets import SecretGetter
import os, sys

#app = Flask(__name__)

class AppConfigBuilder:
    def __init__(self, app, conf_path):
        self.app = app
        self.conf_path = conf_path
        self.secretGetter = SecretGetter(conf_path)

    def getSecret(self, key):
        return self.secretGetter.getSecret(key)

    def setFlaskConfig(self):
        # get raw secrets
        db_user = self.getSecret('db-user')
        db_pass = self.getSecret('db-pass')
        db = self.getSecret('db')
        db_host = self.getSecret('db-host')
        db_port = self.getSecret('db-port')
        app_env = self.getSecret('app-env')
        app_debug = self.getSecret('app-debug')

        # set flask config
        self.app.config['MYSQL_DATABASE_USER'] = db_user
        self.app.config['MYSQL_DATABASE_PASSWORD'] = db_pass
        self.app.config['MYSQL_DATABASE_DB'] = db
        self.app.config['MYSQL_DATABASE_HOST'] = db_host
        self.app.config['MYSQL_DATABASE_PORT'] = db_port
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db}'

        # set environment variables
        os.environ['FLASK_ENVIRONMENT'] = app_env
        os.environ['DEBUG'] = app_debug
