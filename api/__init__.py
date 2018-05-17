from flask import Flask

# create and configure the app
app = Flask(__name__)
# configure app
app.config.from_object('config.DevelopmentConfig')

print(app.config)
# connect DB
# db = MongoEngine(app)

# import all routes
from api.routes import *