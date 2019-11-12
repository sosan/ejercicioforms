"""
FLASK FORMULARIOS Y PARAMETROS DENTRO DE URL

"""

from flask import Flask
from flask import request
from flask import abort
from flask import render_template

from forms.forms import formularioContactar

app = Flask(__name__)
app.debug = True
app.secret_key = "SEEECRETO"


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/contacto", methods=["GET", "POST"])
def contacto():

    contactar = formularioContactar(request.form)

    if request.method == "POST":
        if contactar.validate():
            print("cONTACTAR {0}" .format(contactar.nombre.data))
            print("cONTACTAR {0}".format(contactar.email.data))
            print("cONTACTAR {0}".format(contactar.comentario.data))

            context = {
                "nombre": contactar.nombre.data,
                "email": contactar.email.data,
                "comentario": contactar.comentario.data
            }

        return render_template("login.html", datos=context)

    return render_template("contacto.html", form=contactar)


@app.route("/parametros")
@app.route("/parametros/<otraruta>")
@app.route("/parametros/<otraruta>/<int:entero>")
def param(otraruta="", entero=0):
    print("El parametro enviado: {0} y {1} (por defecto es 0 aunque no le pasemos nada)".format(
        otraruta, entero))
    return render_template("parametros.html", ota=otraruta, inte=entero)


@app.route("/usuarios/<nombre>")
def parame(nombre=""):
    return render_template("ejercicio.html", user=nombre)


@app.route("/ejercicio")
def ejercicio():
    return render_template("ejercicio.html")


if __name__ == '__main__':
    app.run("127.0.0.1", 5000, debug=True)
