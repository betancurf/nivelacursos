from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_login import LoginManager
from flask_login import login_user
from flask_login import logout_user
from modulos.cursos import blue_cursos
from modulos.usuarios import blue_usuarios
from pprint import pprint
from random import sample
from modelos import db
from modelos import PQR
from modelos import Usuario

from bcrypt import gensalt
from bcrypt import hashpw as encriptar_password
from bcrypt import checkpw as confirmar_password

# Zona de configuración de la app principal
app = Flask(__name__)

# Estas configuraciones NO deberían estar aquí. Se debe crear
# un archivo de configuración y este NO debe ser compartido por
# medio de github. Solo están aquí a modo de ejemplo y serán
# removidos en proximas clases...
app.config["DATABASE_URL"] = "sqlite:///db.sqlite3"
app.config["SECRET_KEY"] = "ah fskdbfjha fi23i2b3i4b23kb,m c"

# Zona de inicialización de herramientas
db.init_app(app)  # Inicializa la base de datos con peewee

login_manager = LoginManager()
login_manager.init_app(app)

# Zona de registro de blueprints
app.register_blueprint(blue_cursos, url_prefix="/cursos")
app.register_blueprint(blue_usuarios, url_prefix="/usuarios")


# Zona de funciones de ayuda
@login_manager.user_loader
def user_loader(user_id):
    try:
        user = Usuario.get(Usuario.id == user_id)
        return user
    except:
        return 


# Zona de endpoints

@app.route("/")
@app.route("/index")
@app.route("/inicio")
def inicio():
    info_cursos_destacados = [
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

    info_servicios = [
        {
            "nombre": "Cursos virtuales",
            "logo":"fa-solid fa-truck",
            "descripcion":"Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata",
            "url":"/services",
        },
        {
            "nombre": "Cursos presenciales",
            "logo":"fa-solid fa-address-book",
            "descripcion":"Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata",
            "url":"/services",
        },
        {
            "nombre": "Cursos a empresas",
            "logo":"fa-solid fa-anchor",
            "descripcion":"Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata",
            "url":"/services",
        },
        {
            "nombre": "Cursos de primaria",
            "logo":"fa-solid fa-arrows-to-eye",
            "descripcion":"Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata",
            "url":"/services",
        },
        {
            "nombre": "Cursos de secundaria",
            "logo":"fa-solid fa-bed",
            "descripcion":"Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata",
            "url":"/services",
        },
        {
            "nombre": "Guia para tareas",
            "logo":"fa-solid fa-bicycle",
            "descripcion":"Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata",
            "url":"/services",
        },
    ]

    info_tutores = [
        {
            "nombre":"Fabian Betancur",
            "profesion":"Ing. de sistemas",
            "descripcion":"",
            "url_foto":"static/img/testimonials/testimonials-1.jpg",
            "estrellas": 2,
        },
        {
            "nombre":"Juan C. Parra",
            "profesion":"Batmnan",
            "descripcion":"",
            "url_foto":"static/img/testimonials/testimonials-2.jpg",
            "estrellas": 4,
        },
        {
            "nombre":"Laura A. Carrillo",
            "profesion":"Ing. de software",
            "descripcion":"",
            "url_foto":"static/img/testimonials/testimonials-3.jpg",
            "estrellas": 5,
        },
        {
            "nombre":"Laura Pinzon",
            "profesion":"Ing. ambiental",
            "descripcion":"",
            "url_foto":"static/img/testimonials/testimonials-4.jpg",
            "estrellas": 5,
        },
        {
            "nombre":"Mauricio Martinez",
            "profesion":"Ing. de sistemas",
            "descripcion":"",
            "url_foto":"static/img/testimonials/testimonials-5.jpg",
            "estrellas": 3,
        },
        {
            "nombre":"Diego Rodriguez",
            "profesion":"Diseñador grafico",
            "descripcion":"",
            "url_foto":"static/img/testimonials/testimonials-5.jpg",
            "estrellas": 4,
        }
    ]

    return render_template(
        'estaticas/index.html',
        cursos_destacados=sample(info_cursos_destacados, 3),
        servicios=info_servicios,
        tutores=info_tutores
    )


@app.route("/about")
def about():
    return render_template('estaticas/about.html')


@app.route("/services")
def service():
    return render_template("estaticas/services.html")


@app.route("/faq")
def faq():
    return "Pagina de preguntas frecuentes"


@app.route("/contacto", methods=['GET', 'POST'])
def contacto_f():
    # Si es get, mostrar la pagina normalita
    if request.method == "GET":
        return render_template("estaticas/contact.html")
    
    # Sino, si es POST vamos a guardarlo en la base de datos
    # y mostrar una pagina en blanco con la lista de los pqr realizados a la fecha
    elif request.method == "POST":
        # leemos la información del formulario
        nombre = request.form.get("name")
        email = request.form.get("email")
        asunto = request.form.get("subject")
        mensaje = request.form.get("message")

        # Validamos que ningun campo esté vacio
        if nombre and email and asunto and mensaje:
            # Creamos un nuevo PQR en la base de datos
            PQR.create(
                nombre=nombre,
                email=email,
                asunto=asunto,
                mensaje=mensaje,
            )
            
        # Mostramos un mensaje con todos los PQR creados hasta el momento:
        # No asustarse por esa linea de codigo, simplemente es para no escirbir una pagina completa de html
        msg = f"{'<br>'.join([f'<br><br>{pqr.asunto}: <br>{pqr.mensaje}<br>-{pqr.nombre}, {pqr.email}' for pqr in list(PQR.select())])}"
        return msg


@app.route("/registro", methods=["GET", "POST"])
def registro_f():
    if request.method == "GET":
        return render_template("usuarios/registro.html")
    else:
        nickname = request.form.get("nickname")
        correo = request.form.get("correo")
        password = request.form.get("password")
        nombre = request.form.get("nombre")
        apellidos = request.form.get("apellidos")
        telefono = request.form.get("telefono")

        if nickname and correo and password:
            pass_seguro = encriptar_password( password.encode("utf-8"), gensalt())
            try:
                nuevo_usuario = Usuario.create(
                    nickname=nickname,
                    correo=correo,
                    password=pass_seguro,
                    nombre=nombre,
                    apellidos=apellidos,
                    telefono=telefono,
                    rol="ESTUDIANTE"
                )
                
                login_user(nuevo_usuario)
                return redirect(url_for('app_usuarios.perfil'))
            except Exception as e:
                return f"Error, no se pudo crear el usuario: {e}"
        return "Error, datos incompletos"


@app.route("/ingreso", methods=["GET", "POST"])
def ingreso_f():
    if request.method == "GET":
        return render_template("usuarios/ingreso.html")
    else:
        nickname = request.form.get("nickname")
        password = request.form.get("password")
        if nickname and password:
            try:
                usuario = Usuario.get(nickname=nickname)
            except Exception as e:
                return f"Error, no se pudo obtener el usuario"

            pass_actual = usuario.password
            hacen_match = confirmar_password(password.encode("utf-8"), pass_actual.encode("utf-8"))

            if hacen_match:
                login_user(usuario)
                return redirect(url_for('app_usuarios.perfil'))
            else:
                return f"Error, usuario o contraseña no validos"            
        return "Error, datos incompletos"


@app.route("/salir")
def salir_f():
    logout_user()
    return redirect(url_for("inicio"))

if __name__ == "__main__":
    app.run(debug=True)
