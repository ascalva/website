import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test-secret-key'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG   = True
    TESTING = True
    ENV     = 'development'

