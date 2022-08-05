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
    info_servicios = [
        {
            "url_foto": "img/storage-service.jpg",
            "nombre":"Storage",
            "descripcion":"Cumque eos in qui numquam. Aut aspernatur perferendis sed atque quia voluptas quisquam repellendus temporibus itaqueofficiis odit",
        },
        {
            "url_foto": "img/logistics-service.jpg",
            "nombre":"Logistics",
            "descripcion":"Asperiores provident dolor accusamus pariatur dolore nam id audantium ut et iure incidunt molestiae dolor ipsam ducimus occaecati nisi",
        },
        {
            "url_foto": "img/cargo-service.jpg",
            "nombre":"Cargo",
            "descripcion":"Dicta quam similique quia architecto eos nisi aut ratione aut ipsum reiciendis sit doloremque oluptatem aut et molestiae ut et nihil",
        },
        {
            "url_foto": "img/trucking-service.jpg",
            "nombre":"Trucking",
            "descripcion":"Dicta quam similique quia architecto eos nisi aut ratione aut ipsum reiciendis sit doloremque oluptatem aut et molestiae ut et nihil",
        },
        {
            "url_foto": "img/packaging-service.jpg",
            "nombre":"Packaging",
            "descripcion":"Illo consequuntur quisquam delectus praesentium modi dignissimos facere vel cum onsequuntur maiores beatae consequatur magni voluptates",
        },
        {
            "url_foto": "img/warehousing-service.jpg",
            "nombre":"Warehousing",
            "descripcion":"Quas assumenda non occaecati molestiae. In aut earum sed natus eatae in vero. Ab modi quisquam aut nostrum unde et qui est non quo nulla",
        },
    ]

    return render_template(
        'estaticas/index.html',
        servicios=sample(info_servicios, 3)
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
