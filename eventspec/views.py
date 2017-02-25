import yaml

from eventspec.blueprints import api, home
from flask import jsonify, render_template, request


@api.route("/healthcheck")
def health_check():
    return jsonify(status="success")


@api.route("/convert")
def convert():
    text = request.args.get('source', None)
    if text is None:
        return jsonify(status="failure", error="No source yaml found")

    text = text.replace("\t", "    ")
    try:
        obj = yaml.load(text)
        res = render_template("template.html", properties=obj)
        return jsonify(status="success", result=res)
    except Exception as e:
        return jsonify(status="failure", error=e.message)


@home.route("/")
def index():
    return render_template("index.html")