from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/animales_exoticos")
def animales():
    animal = ["Foca monje del Caribe", "Gato", "Elefante", "León", "Tigre", "Jirafa", "Canguro", "Mono", "Rinoceronte", "Hipopótamo"]
    return render_template("animales.html", animales=animal)

@app.route("/vehiculos_antiguos")
def vehiculos():
    return render_template("vehiculos.html")

@app.route("/maravillas_mundo")
def maravillas():
    return render_template("maravillas.html")

@app.route("/acerca_de")
def acerca():
    return render_template("acerca.html")

if __name__ == "__main__":
    app.run(debug=True)