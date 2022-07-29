from flask import Blueprint
from modulos.examenes import blue_examenes

blue_cursos = Blueprint("app_cursos", __name__)
blue_cursos.register_blueprint(blue_examenes, url_prefix="/examenes")


@blue_cursos.route("/lista")
def lista():
    return "Aqui va la lista de cursos"
