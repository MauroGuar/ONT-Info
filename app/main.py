from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", css_file="index_styles.css")


@app.route("/buscar", methods=["POST"])
def buscar():
    if request.method == "POST":
        olt_ip = request.form["olt_ip"]
        ont_sn = request.form["ont_sn"]
        resultado = f"OLT IP: {olt_ip}, ONT SN: {ont_sn}"
        return render_template(
            "resultado.html", css_file="main_styles.css", resultado=resultado
        )
