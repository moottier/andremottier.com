from flask import Flask
from .util import SecretGetter
import yaml
import os, sys

class AppConfigBuilder:
    def __init__(self, app, conf_path, secret_path):
        self.app = app
        self.conf_path = conf_path
        self.secret_path = secret_path
        self.secretGetter = SecretGetter(secret_path)    # TODO: don't need local file to be encrypted
        self._conf = yaml.safe_load(conf_path)
        self._secrets = yaml.safe_load(secret_path)

    def getSecret(self, key):
        #return self.secretGetter.getSecret(key)
        return self._secrets[key]

    def getConf(self, key):
        return self._conf[key]

    def setFlaskConfig(self):
        # get raw secrets
        db_user = self.getConf('db-user')
        db = self.getConf('db')
        db_host = self.getConf('db-host')
        db_port = self.getConf('db-port')
        app_env = self.getConf('app-env')
        app_debug = self.getConf('app-debug')
        
        app_key = self.getSecret('app-key')
        db_pass = self.getSecret('db-pass')

        # set flask config
        self.app.config['SECRET_KEY'] = app_key
        self.app.config['FLASK_ENVIRONMENT'] = app_env
        self.app.config['DEBUG'] = app_debug
        
        self.app.config['MYSQL_DATABASE_USER'] = db_user
        self.app.config['MYSQL_DATABASE_PASSWORD'] = db_pass
        self.app.config['MYSQL_DATABASE_DB'] = db
        self.app.config['MYSQL_DATABASE_HOST'] = db_host
        self.app.config['MYSQL_DATABASE_PORT'] = db_port
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db}'        
