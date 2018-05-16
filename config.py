# From http://flask.pocoo.org/docs/0.12/config/#Development-from-files

# This file manages our env variables and different configurations.

# Base Config
class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_DB = 'main'

# These classes inherit Config and change something about it
class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
