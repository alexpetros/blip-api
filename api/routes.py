from api import app
from flask import jsonify

@app.route('/')
def hello():
    defaultResponse = {
        'text': 'Hello World!',
    }

    return jsonify(defaultResponse)