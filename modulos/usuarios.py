from flask import Blueprint
from flask import render_template
from flask_login import login_required
from flask_login import current_user

from modelos import Curso
from modelos import UsuarioCurso
from modelos import Usuario

blue_usuarios = Blueprint("app_usuarios", __name__)

@blue_usuarios.route("/perfil")
@login_required
def perfil_f():

    mis_cursos = UsuarioCurso.select().where(UsuarioCurso.usuario == current_user)

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




