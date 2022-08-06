from flask import Blueprint

blue_usuarios = Blueprint("app_usuarios", __name__)

@blue_usuarios.route("/perfil")
def perfil():
    return "Perfil del usuario"
