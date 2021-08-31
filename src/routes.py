from flask               import render_template, flash, redirect, url_for, request, make_response, jsonify, Blueprint
from flask_login         import current_user, login_user, logout_user, login_required
from werkzeug.urls       import url_parse
from src                 import app


api = Blueprint('api', __name__, url_prefix="/")

@api.route("/", methods=['GET'])
def index() :
    return jsonify("hello world")

