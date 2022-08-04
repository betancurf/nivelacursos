from flask import Flask
from flask import render_template
from flask import request
from modulos.cursos import blue_cursos
from pprint import pprint

app = Flask(__name__)
app.register_blueprint(blue_cursos, url_prefix="/cursos")


@app.route("/")
@app.route("/index")
@app.route("/inicio")
def inicio():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/services")
def service():
    return render_template("services.html")


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
        return render_template("contact.html")
    
    # Sino, si es POST vamos a hacer alguna cosas
    elif request.method == "POST":
        # Si en el POST se envio un nombre igual a Fabian, redireccionar al index
        # if  request.form["name"] == "Fabian":
        #     return redirect(url_for('inicio'))

        # Cualquiero otro nombre recibe este mensaje:
        return msg


if __name__ == "__main__":
    app.run(debug=True)
