# From http://flask.pocoo.org/docs/0.12/config/#Development-from-files

# This file manages our env variables and different configurations.

# Base Config
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''

# These classes inherit Config and change something about it
class ProductionConfig(Config):
    DATABASE_URI = ''

class DevelopmentConfig(Config):
    DEBUG = True
