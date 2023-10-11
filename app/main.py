from datetime import datetime
from flask import Flask, render_template, request
from app.data_processing.ont_info import get_ont_info
from app.data_processing.errors import personalized_exception
from app.data_processing.connection_db import DataBase  

app = Flask(__name__)
db = DataBase()
history_data = []

@app.route("/")
def index():
    return render_template("index.html", css_file="index_styles.css")


@app.route("/buscar", methods=["POST"])
def buscar():
    if request.method == "POST":
        olt_ip = request.form["olt_ip"]
        ont_sn = request.form["ont_sn"]
        try:
            info_dictionaries = get_ont_info(olt_ip, ont_sn, False)
            date = datetime.now().strftime("%Y-%m-%d")
            time = datetime.now().strftime("%H:%M:%S")

            data = {   
                "olt_ip": olt_ip,
                "ont_sn": ont_sn,
                "date": date,   
                "time": time,
                "informacion_olt": info_dictionaries    
            }
            db.save_mongo(data)

            return render_template(
                "results.html", css_file="results_styles.css", info_dictionaries=info_dictionaries, olt_ip=olt_ip, ont_sn=ont_sn, date=date, time=time
            )
        except personalized_exception as e:
            
            return render_template(
                "index.html", css_file="index_styles.css", e=e
            )

@app.route("/history" , methods=["POST"])
def history():
    olt_ip = request.form['olt_ip']
    ont_sn = request.form['ont_sn']

    history_data = db.get_mongo(olt_ip, ont_sn)

    for item in history_data:
        item['_id'] = str(item['_id'])

    return render_template("history.html", css_file="history_styles.css", historial=history_data)