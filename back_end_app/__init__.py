from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'
from back_end_app.api import routes


if __name__ == '__main__':
    app.run()