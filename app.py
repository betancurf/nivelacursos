from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from modulos.cursos import blue_cursos
from pprint import pprint
from random import sample

app = Flask(__name__)
app.register_blueprint(blue_cursos, url_prefix="/cursos")


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
    print(f"---> Estoy en pagina de contacto, con metodo: {request.method}")
    pprint(request.args)
    pprint(request.form)

    msg = f"""
        Mensaje enviado con exito
        <br>
        Valores del query string: {request.args}
        <br>
        Valores del formulario: {request.form}
        """
    
    pprint(msg)

    # Si es get, mostrar la pagina normalita
    if request.method == "GET":
        # return f"Se hizo get con los siguientes parametros: {request.args}"
        return render_template("estaticas/contact.html")
    
    # Sino, si es POST vamos a hacer alguna cosas
    elif request.method == "POST":
        # Si en el POST se envio un nombre igual a Fabian, redireccionar al index
        # if  request.form["name"] == "Fabian":
        #     return redirect(url_for('inicio'))

        # Cualquiero otro nombre recibe este mensaje:
        return msg


if __name__ == "__main__":
    app.run(debug=True)
