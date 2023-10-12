from datetime import datetime
import pytz
from flask import Flask, render_template, request
from app.data_processing.ont_info import get_ont_info_to_show

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", css_file="index_styles.css")


@app.route("/buscar", methods=["POST"])
def buscar():
    if request.method == "POST":
        olt_ip = request.form["olt_ip"]
        ont_sn = request.form["ont_sn"]

        date = datetime.now().strftime("%d/%m/%Y")
        time = datetime.now(pytz.timezone('America/Argentina/Buenos_Aires')).strftime('%H:%M')

        items_to_show = ["run state", "temperature(c)", "description", "last down cause", "last up time",
                         "last down time", "ont online duration", "rx optical power(dbm)",
                         "olt rx ont optical power(dbm)"]
        dictionary_to_show = get_ont_info_to_show(olt_ip, ont_sn, items_to_show, False)

        return render_template(
            "results.html", css_file="results_styles.css", olt_ip=olt_ip, ont_sn=ont_sn, date=date, time=time,
            dict_show=dictionary_to_show
        )
