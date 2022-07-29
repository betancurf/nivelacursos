from flask import Flask
from modulos.cursos import blue_cursos

app = Flask(__name__)
app.register_blueprint(blue_cursos, url_prefix="/cursos")

@app.route("/")
@app.route("/index")
@app.route("/inicio")
def index():
    return "Bienvenido a nuestra app"

@app.route("/faq")
def index():
    return "Pagina de preguntas frecuentes"

if __name__ == "__main__":
    app.run()
