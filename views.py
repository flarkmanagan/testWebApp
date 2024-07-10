from flask import Blueprint, render_template, jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Mark")

@views.route("/json")
def get_json():
    return jsonify({'name': 'mark', 'age': 30})