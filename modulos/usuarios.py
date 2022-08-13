from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import flash
from flask import url_for
from flask_login import login_required
from flask_login import current_user
from enums import FlashCat
from modelos import Curso
from modelos import UsuarioCurso
from modelos import Usuario
from modelos import SolicitudParaProfesor

blue_usuarios = Blueprint("app_usuarios", __name__)

@blue_usuarios.route("/perfil")
@login_required
def perfil_f():
    # # Para obtener los cursos del usuario, pueden ejecutar este query
    # mis_cursos = list(UsuarioCurso.select().where(UsuarioCurso.usuario == current_user))

    # O alternativamente, usar el backreference creado en la clase Usuario desde la clase UsuarioCurso
    mis_cursos = current_user.cursos

    # # Puedo consultar los cursos creados por este usuario mediante esta query:
    # cursos_creados = list(Curso.select().where(Curso.creador == current_user))

    # Alternativamente, si en el modelo se ha definido una backref 
    # (referencia hacia atras o referencia inversa o reversa)
    # puedo usar directamente el nombre del backref para obtener la información
    cursos_creados = list(current_user.cursos_creados)

    return render_template(
        "/usuarios/perfil.html",
        mis_cursos=mis_cursos,
        cursos_creados=cursos_creados,
        roles=Usuario.ROLES
    )


@blue_usuarios.route("/solitud_para_profesor")
@login_required
def solitud_para_profesor_f():
    flash("Solicitud enviada con exito", FlashCat.EXITO.value)
    SolicitudParaProfesor.create(solicitante=current_user)
    return redirect(url_for("app_usuarios.perfil_f"))
