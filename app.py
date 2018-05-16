from flask import Flask
app = Flask(__name__)

# Set up env variables & config
app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()