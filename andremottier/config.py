from flask import Flask
from andremottier.util import SecretGetter
import yaml
import os, sys

class Config:
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
