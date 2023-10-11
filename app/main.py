from flask import Flask, render_template, request
from app.data_processing.ont_info import get_ont_info

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", css_file="index_styles.css")


@app.route("/buscar", methods=["POST"])
def buscar():
    if request.method == "POST":
        olt_ip = request.form["olt_ip"]
        ont_sn = request.form["ont_sn"]

        resultado = get_ont_info(olt_ip, ont_sn, True)

        return render_template(
            "results.html", css_file="results_styles.css", resultado=resultado
        )
