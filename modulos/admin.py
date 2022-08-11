from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import flash
from flask_login import current_user
from flask_login import login_required
from enums import FlashCat as cat
from modelos import SolicitudParaProfesor
from modelos import Usuario

blue_admin = Blueprint("app_admin", __name__)


@blue_admin.route("/solicitudes")
@login_required
def solicitudes_f():
    if not current_user.rol == Usuario.ROLES.ADMIN.value:
        flash("Usted no debería estar aquí", cat.ALERTA.value)
        return redirect(url_for("inicio"))

    solicitudes = SolicitudParaProfesor.select()
    return render_template(
        "admin/solicitudes.html",
        solicitudes=solicitudes
    )

@blue_admin.route("/solicitudes/aceptar/<id_solicitud>")
@login_required
def aceptar_solicitud_f(id_solicitud):
    if not current_user.rol == Usuario.ROLES.ADMIN.value:
        return "Usted no debería estar aquí"

    try:
        solicitud = SolicitudParaProfesor.get(SolicitudParaProfesor.id==id_solicitud)
        solicitud.solicitante.rol = Usuario.ROLES.PROFESOR.value
        solicitud.solicitante.save()
        solicitud.delete_instance()
        flash("Profesor aceptado con exito")
    except:
        flash("Solicitud no encontrada", cat.FALLA.value)

    return redirect(url_for("app_admin.solicitudes_f"))

@blue_admin.route("/solicitudes/denegar/<id_solicitud>")
@login_required
def denegar_solicitud_f(id_solicitud):
    if not current_user.rol == Usuario.ROLES.ADMIN.value:
        return "Usted no debería estar aquí"

    try:
        solicitud = SolicitudParaProfesor.get(SolicitudParaProfesor.id==id_solicitud)
        # solicitud.solicitante.rol = Usuario.ROLES.PROFESOR.value
        solicitud.delete_instance()
        flash("Profesor denegado con exito", cat.INFO.value)
    except:
        flash("Solicitud no encontrada", cat.FALLA.value)

    return redirect(url_for("app_admin.solicitudes_f"))