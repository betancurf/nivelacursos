from flask import Blueprint
from flask import redirect
from flask import url_for

blue_examenes = Blueprint("app_examenes", __name__)


@blue_examenes.route("/")
def index_f():
    return "bienvenido al examen"


@blue_examenes.route("/lista")
def lista_f():
    return "Aqui va la lista de los examenes"


@blue_examenes.route("/ver")
@blue_examenes.route("/ver/<int:id_examen>")
def ver_f(id_examen=None):
    if id_examen:
        return f"Usted está viendo el resultado del examen {id_examen}"
    return redirect( url_for("app_cursos.app_examenes.lista_f") )
