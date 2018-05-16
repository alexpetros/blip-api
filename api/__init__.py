from flask import Flask

# create and configure the app
app = Flask(__name__)
# configure app
app.config.from_object('config.DevelopmentConfig')

print(app.config)
# connect DB
# db = MongoEngine(app)

# a simple page that says hello
from api.routes import *