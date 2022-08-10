from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from modulos.examenes import blue_examenes
from modelos import Curso

blue_cursos = Blueprint("app_cursos", __name__)
blue_cursos.register_blueprint(blue_examenes, url_prefix="/examenes")


@blue_cursos.route("/crear", methods=["GET", "POST"])
@login_required
def crear_f():
    if request.method == "GET":
        return render_template("cursos/crear.html")
    
    elif request.method == "POST":
        nombre = request.form.get("nombre")
        url_foto = request.form.get("url_foto")
        descripcion = request.form.get("descripcion")

        if nombre and url_foto and descripcion:
            curso = Curso.create(
                nombre=nombre,
                url_foto=url_foto,
                descripcion=descripcion,
                creador=current_user
            )
            return redirect(url_for("app_cursos.detalle_f"))
        else:
            return "Error, información incompleta"            


@blue_cursos.route("/detalles/<uuid:id_curso>")
def detalle_f(id_curso):
    # breakpoint()
    try:
        curso = Curso.get(id=id_curso)
    except:
        return "Error, curso no encontrado."

    return render_template(
        "cursos/detalles.html",
        info_curso=curso
    )

@blue_cursos.route("/lista")
def lista():
    return "Aqui va la lista de cursos"
