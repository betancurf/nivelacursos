from flask import Blueprint
from flask_login import login_required
from flask import render_template

blue_admin = Blueprint("app_admin", __name__)

@blue_admin.route("/")
@login_required
def ver_f():
    return render_template("admin/administrar_profesores.html")

@blue_admin.route("/")
def aceptar_f():
    return "aquí iría la misma url de admin pero con la socicitud que acepté  abajo en las editables"

@blue_admin.route("/")
def denegar_f():
    return "aquí iría la misma url de admin pero que la socicitud que acepté desaparezca"