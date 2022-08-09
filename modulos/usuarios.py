from flask import Blueprint
from flask import render_template
from flask_login import login_required
from flask_login import current_user

from modelos import Curso, UsuarioCurso

blue_usuarios = Blueprint("app_usuarios", __name__)

@blue_usuarios.route("/perfil")
@login_required
def perfil_f():
    mis_cursos = [
        {
            "url_foto": "img/storage-service.jpg",
            "nombre":"Programación en Java",
            "descripcion":"Cumque eos in qui numquam. Aut aspernatur perferendis sed atque quia voluptas quisquam repellendus temporibus itaqueofficiis odit",
        },
        {
            "url_foto": "img/logistics-service.jpg",
            "nombre":"Programación en Python",
            "descripcion":"Asperiores provident dolor accusamus pariatur dolore nam id audantium ut et iure incidunt molestiae dolor ipsam ducimus occaecati nisi",
        },
        {
            "url_foto": "img/cargo-service.jpg",
            "nombre":"Programación web",
            "descripcion":"Dicta quam similique quia architecto eos nisi aut ratione aut ipsum reiciendis sit doloremque oluptatem aut et molestiae ut et nihil",
        },
        {
            "url_foto": "img/trucking-service.jpg",
            "nombre":"O.O.P",
            "descripcion":"Dicta quam similique quia architecto eos nisi aut ratione aut ipsum reiciendis sit doloremque oluptatem aut et molestiae ut et nihil",
        },
        {
            "url_foto": "img/packaging-service.jpg",
            "nombre":"Bases de datos",
            "descripcion":"Illo consequuntur quisquam delectus praesentium modi dignissimos facere vel cum onsequuntur maiores beatae consequatur magni voluptates",
        },
        {
            "url_foto": "img/warehousing-service.jpg",
            "nombre":"SQL",
            "descripcion":"Quas assumenda non occaecati molestiae. In aut earum sed natus eatae in vero. Ab modi quisquam aut nostrum unde et qui est non quo nulla",
        },
    ]

    # mis_cursos = []

    mis_cursos = UsuarioCurso.select().where(UsuarioCurso.usuario == current_user)

    # Puedo consultar los cursos creados por este usuario mediante esta query:
    cursos_creados = list(Curso.select().where(Curso.creador == current_user))

    # Alternativamente, si en el modelo se ha definido una backref 
    # (referencia hacia atras o referencia inversa o reversa)
    # puedo usar directamente el nombre del backref para obtener la información
    cursos_creados = list(current_user.cursos_creados)
    # breakpoint()
    return render_template(
        "/usuarios/perfil.html",
        mis_cursos=mis_cursos,
        cursos_creados=cursos_creados,
    )




