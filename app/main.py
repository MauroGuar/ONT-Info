import datetime

import pytz
from flask import Flask, render_template, request
from app.data_processing.ont_info import new_request, query_refresh
from app.config import MONGO_URI
from app.database.connection import init_db

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
init_db(app)


@app.route("/")
def index():
    return render_template("index.html", css_file="index_styles.css")


@app.route("/buscar", methods=["POST"])
def buscar():
    if request.method == "POST":
        olt_ip = request.form["olt_ip"]
        ont_sn = request.form["ont_sn"]

        items_to_show = [
            "run state",
            "temperature(c)",
            "description",
            "last down cause",
            "last up time",
            "last down time",
            "ont online duration",
            "rx optical power(dbm)",
            "olt rx ont optical power(dbm)",
        ]

        debug_mode = False

        if "refresh-info" in request.form:
            date, time, dictionary_to_show = query_refresh(
                olt_ip, ont_sn, items_to_show=items_to_show, debug_mode=debug_mode
            )
        else:
            date, time, dictionary_to_show = new_request(
                olt_ip, ont_sn, items_to_show=items_to_show, debug_mode=debug_mode
            )

        return render_template(
            "results.html",
            css_file="results_styles.css",
            olt_ip=olt_ip,
            ont_sn=ont_sn,
            date=date,
            time=time,
            dictionary_to_show=dictionary_to_show,
        )
