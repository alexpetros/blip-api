from flask import Flask, jsonify
app = Flask(__name__)

# Set up env variables & config & db
app.config.from_object('config.DevelopmentConfig')
db = MongoEngine(app)

@app.route('/')
def hello():
    defaultResponse = {
        'text': 'Hello World!',
    }

    return jsonify(defaultResponse)


if __name__ == '__main__':
    app.run()