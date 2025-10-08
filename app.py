from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    arr = ["Luis","Kemia","Gerardo","Arturo"]
    autor ="jesus Antonio Sagarnaga Macias"
    return render_template("index.html" , nombre=autor , amigos=arr)

if __name__ == "__main__":
    app.run(debug=True)