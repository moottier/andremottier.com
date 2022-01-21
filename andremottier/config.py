from flask import Flask
from andremottier.util import SecretGetter
import yaml
import os, sys

#TODO: use Flask config api

class Config:
    """
    This class will replace AppConfigBuilder
    currently it is only used to send in config for testing
    """
    SECRET_KEY = None
    FLASK_ENVIRONMENT = "production"
    DEBUG = False
    MYSQL_DATABASE_USER = None
    MYSQL_DATABASE_PASSWORD = None
    MYSQL_DATABASE_DB = None
    MYSQL_DATABASE_HOST = None
    MYSQL_DATABASE_PORT = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = None
    REGISTRATION_ALLOWED = False
    SECRETS_PATH = None
    SQLALCHEMY_DATABASE_URI = None

    def __init__(self):
        if self.SECRETS_PATH:
            with open(self.SECRETS_PATH, 'r') as strm:
                self._secrets = yaml.safe_load(strm)
            Config.SECRET_KEY = self.getSecret('app-secret')
            Config.MYSQL_DATABASE_PASSWORD = self.getSecret('db-pass')
            Config.SQLALCHEMY_DATABASE_URI = f'mysql://{self.MYSQL_DATABASE_USER}:{self.MYSQL_DATABASE_PASSWORD}@{self.MYSQL_DATABASE_HOST}:{self.MYSQL_DATABASE_PORT}/{self.MYSQL_DATABASE_DB}'

    def getSecret(self, key):
        return self._secrets[key]

class ProductionConfig(Config):
    MYSQL_DATABASE_USER = "www-db"
    MYSQL_DATABASE_DB = "andremottier"
    MYSQL_DATABASE_HOST = "localhost"
    MYSQL_DATABASE_PORT = "3306"
    SECRETS_PATH = r'/var/www/andremottier.com/secrets.yaml'

class DevelopmentConfig(Config):
    FLASK_ENVIRONMENT = "development"
    DEBUG = True
    MYSQL_DATABASE_USER = "www-db"
    MYSQL_DATABASE_DB = "andremottier"
    MYSQL_DATABASE_HOST = "localhost"
    MYSQL_DATABASE_PORT = "3306"
    SECRETS_PATH = r'/var/www/dev.andremottier.com/secrets.yaml'


class AppConfigBuilder:
    def __init__(self, app, conf_path, secret_path):
        self.app = app
        self.conf_path = conf_path
        self.secret_path = secret_path
        with open(conf_path, 'r') as strm_1, open(secret_path, 'r') as strm_2:
            self._conf = yaml.safe_load(strm_1)
            self._secrets = yaml.safe_load(strm_2)

        # settings that are always applied
        self.app.jinja_options["trim_blocks"] = True
        self.app.jinja_options["lstrip_blocks"] = True

    def getSecret(self, key):
        return self._secrets[key]

    def getConf(self, key):
        return self._conf[key]

    def setFlaskConfig(self):
        # get settings
        db_user = self.getConf('db-user')
        db = self.getConf('db')
        db_host = self.getConf('db-host')
        db_port = self.getConf('db-port')
        app_env = self.getConf('app-env')
        app_debug = self.getConf('app-debug')
        
        app_secret = self.getSecret('app-secret')
        db_pass = self.getSecret('db-pass')

        registration_allowed = self.getConf('registration-allowed')

        # set flask config
        self.app.config['SECRET_KEY'] = app_secret
        self.app.config['FLASK_ENVIRONMENT'] = app_env
        self.app.config['DEBUG'] = app_debug
        
        self.app.config['MYSQL_DATABASE_USER'] = db_user
        self.app.config['MYSQL_DATABASE_PASSWORD'] = db_pass
        self.app.config['MYSQL_DATABASE_DB'] = db
        self.app.config['MYSQL_DATABASE_HOST'] = db_host
        self.app.config['MYSQL_DATABASE_PORT'] = db_port
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db}'

        self.app.config['REGISTRATION_ALLOWED'] = registration_allowed
