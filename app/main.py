# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, session
from json import loads
from app.data_processing.ont_info import new_request, query_refresh
from app.config import MONGO_URI, FLASK_SESSION_SECRET_KEY
from app.database.connection import init_db
from app.data_processing.error_handler.errors import personalized_exception

# Create a Flask web application instance
app = Flask(__name__)

# Set the session secret key
app.secret_key = FLASK_SESSION_SECRET_KEY

# Configure the MongoDB URI for the application
app.config["MONGO_URI"] = MONGO_URI

# Initialize the database connection for the Flask app
init_db(app)


# Define a route for the root URL ("/")
@app.route("/")
def index():
    """
    This function defines the behavior for the root URL ("/").
    It renders an HTML template called "index.html" and passes a CSS file ("index_styles.css") to the template.
    """
    return render_template("index.html", css_file="index_styles.css")


# Define a route for handling POST requests to "/buscar"
@app.route("/buscar", methods=["POST"])
def buscar():
    try:
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

            debug_mode = True

            if "refresh-info" in request.form:
                date, time, dictionary_to_show = query_refresh(
                    olt_ip, ont_sn, items_to_show=items_to_show, debug_mode=debug_mode
                )
            else:
                date, time, dictionary_to_show = new_request(
                    olt_ip, ont_sn, items_to_show=items_to_show, debug_mode=debug_mode
                )

            session['olt_ip'] = olt_ip
            session['ont_sn'] = ont_sn
            session['date'] = date
            session['time'] = time
            session['dictionary_to_show'] = dictionary_to_show

            return redirect(url_for('resultado'))
    except personalized_exception as e:
        return render_template("index.html", css_file="index_styles.css", e=e)


@app.route("/resultado")
def resultado():
    # Recupera los datos de la sesión
    olt_ip = session.get('olt_ip')
    ont_sn = session.get('ont_sn')
    date = session.get('date')
    time = session.get('time')
    dictionary_to_show = session.get('dictionary_to_show', {})

    return render_template(
        "results.html",
        css_file="results_styles.css",
        olt_ip=olt_ip,
        ont_sn=ont_sn,
        date=date,
        time=time,
        dictionary_to_show=dictionary_to_show,
    )


@app.route("/ayuda")
def help():
    return render_template("help.html", css_file="help_styles.css")
