from flask import Flask, render_template, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/animales_exoticos")
def animales():
    animales = [
            {"nombre":"Tapir (Tapirus) ",
            "informacion":"El tapir es un mamífero grande y herbívoro que habita en zonas boscosas de américa del sur, américa central y el sudeste asiático. Se trata de una de las familias más antiguas desde hace unos 55 millones de años, lo que lo convierte en uno de los animales exóticos del mundo.",
            "imagen":"/static/imagenes/tapir_tapirus_3774_2_600.webp"},
            
            {"nombre":"Escalopendra gigante (Scolopendra gigantea)",
            "informacion":"La escalopendra gigante o Scolopendra gigantea es una especie de ciempiés gigante que se encuentra en las tierras bajas de Venezuela, Colombia, islas de Trinidad y Jamaica. Se trata de un animal carnívoro que se alimenta de reptiles, anfibios, e incluso mamíferos como ratones y murciélagos.",
            "imagen":"static/imagenes/escalopendra_gigante_scolopendra_gigantea_3774_4_600.webp"},
            
            {"nombre":"Dragones de mar (Phycodurus eques)"}
        ]
    return render_template("animales.html", animal=animales)

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