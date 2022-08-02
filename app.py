from flask import Flask, render_template
from modulos.cursos import blue_cursos

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

@app.route("/faq")
def faq():
    return "Pagina de preguntas frecuentes"

if __name__ == "__main__":
    app.run(debug=True)
