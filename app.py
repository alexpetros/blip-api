from flask import Flask, jsonify
app = Flask(__name__)

# Set up env variables & config
app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def hello():
    defaultResponse = {
        'text': 'Hello World!',
    }

    return jsonify(defaultResponse)


if __name__ == '__main__':
    app.run()