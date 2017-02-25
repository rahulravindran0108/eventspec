from flask import Blueprint, jsonify

api = Blueprint('api', __name__, template_folder="templates", url_prefix="/api/v1")
home = Blueprint('app', __name__, template_folder="templates", static_folder="static")

