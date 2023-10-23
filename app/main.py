# Import necessary modules
import datetime
import pytz
from flask import Flask, render_template, request
from app.data_processing.ont_info import new_request, query_refresh
from app.config import MONGO_URI
from app.database.connection import init_db
from app.data_processing.error_handler.errors import personalized_exception

# Create a Flask web application instance
app = Flask(__name__)

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
            # Retrieve data from the POST request
            olt_ip = request.form["olt_ip"]
            ont_sn = request.form["ont_sn"]

            # Define a list of items to show on the results page
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

            # Set debug mode to False by default
            debug_mode = True

            # Check if "refresh-info" is in the request form
            if "refresh-info" in request.form:
                # Call the query_refresh function to obtain data
                date, time, dictionary_to_show = query_refresh(
                    olt_ip, ont_sn, items_to_show=items_to_show, debug_mode=debug_mode
                )
            else:
                # Call the new_request function to obtain data
                date, time, dictionary_to_show = new_request(
                    olt_ip, ont_sn, items_to_show=items_to_show, debug_mode=debug_mode
                )

            # Render the "results.html" template with the obtained data
            return render_template(
                "results.html",
                css_file="results_styles.css",
                olt_ip=olt_ip,
                ont_sn=ont_sn,
                date=date,
                time=time,
                dictionary_to_show=dictionary_to_show,
            )
    except personalized_exception as e:
        # Handle a specific custom exception by rendering the "index.html" template and passing the exception (e) for display
        return render_template("index.html", css_file="index_styles.css", e=e)
