from flask      import Flask, Blueprint, request, jsonify
from flask_cors import CORS
from src.config import Config

app = Flask(__name__)
CORS(app)


from src.routes import api

app.register_blueprint(api)
