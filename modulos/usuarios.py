from flask import Blueprint
from flask_login import login_required
from flask_login import current_user

blue_usuarios = Blueprint("app_usuarios", __name__)

@blue_usuarios.route("/perfil")
@login_required
def perfil():
    return f"Perfil del usuario: {current_user.nickname}"
