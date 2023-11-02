# Program Structure

The structure of the program is mainly made based on Flask's structuring standards, with some personal modifications.  
The project is divided into two large sections, the project path "/" and the "app/" directory.  
In the main directory, there are the files for the execution and explanation of the program.  
In the app directory you will find the files and modules with the code necessary for the program to function.

## Inside /app/

### /app/main.py

The `main.py` file is the main entry point of the Flask web application. It sets up the Flask application, configures and initializes a MongoDB database connection, and defines routes for handling different URLs. Each route is associated with a function that processes data and returns a response to the client. The functions handle tasks such as rendering HTML templates, processing form data, storing results in session variables, and redirecting to other routes.

### /app/config.py

The `config.py` file is responsible for managing the configuration of the application. It finds and loads the `.env` file from the project directory. This file contains environment variables that are used throughout the application. The `config.py` file retrieves these variables.

### /app/.env and /app/.env.example

The `.env` and `.env.example` files are used to store environment variables for the application. These variables include `OLT_USERNAME` and `OLT_PASSWORD` for SSH connection credentials to an OLT device, `MONGO_URI` for the MongoDB connection URI, and `FLASK_SESSION_SECRET_KEY` for the secret key used in Flask sessions. The `.env.example` file serves as a template, while the actual values are stored in the `.env` file. The values are kept empty in the `.env.example` file for security reasons, and actual values should be filled in the `.env` file on the local machine.  
It is important to add that the `.env` file is ignored by git in the `.gitignore` file, so the secret credentials are not published.

### /app/data_processing/

The `data_processing` module is responsible for collecting, processing, and returning data from the entire application.  

### /app/data_processing/ont_info.py

The `ont_info.py` file is like the "main" of the entire `data_processing` module because it calls and uses all functions of the rest of the internal modules in order.  
It contains functions for handling and processing data related to Optical Line Terminal (OLT) and Optical Network Terminal (ONT) devices. It includes functions to format time, convert query results into a user-friendly format, refresh queries by creating new ones for specific OLT IP and ONT serial numbers, and make new requests for specific OLT IP and ONT serial numbers. These functions are used to manage and process data from the OLT and ONT devices, handle queries related to these devices, and present the data in a suitable format.

### /app/data_processing/ssh_prompt_handler/

The `ssh_prompt_handler` module is responsible for establishing the ssh connection with the OLT, collecting and validating the ONT data and transforming it into dictionary format.

### /app/data_processing/ssh_prompt_handler/dictionary_converter.py

The `dictionary_converter.py` file is like the "main" of the ssh `prompt_handler_module` because it calls and uses all functions of modules in order.  
It is responsible for converting and returning the data collected from the ONT devices via the SSH connection with the OLT into a dictionary format. This conversion facilitates easier data manipulation and processing within the application.

### /app/data_processing/ssh_prompt_handler/session_spawn.py

The `session_spawn.py` is responsible for establishing and managing the SSH session with the OLT. It may handle tasks such as initiating the connection, handling authentication, and managing the session lifecycle.

### /app/data_processing/ssh_prompt_handler/ont_prompt.py

The `ont_prompt.py` file interacts with the ONT devices via the established SSH session. It handles tasks such as sending commands to the ONT, parsing the responses, and handling any errors or exceptions that occur during the interaction. In the end it returns the prompt obtained from the ONT.

### /app/data_processing/ssh_prompt_handler/prompt_analysis.py

The `prompt_analysis.py` extracts key-value pairs from the ONT prompt and returns them as a dictionary. It uses a regular expression to match key-value pairs in the table prompt, where keys and values are separated by colons. The function initializes an empty dictionary, finds all matches using the regular expression pattern, iterates through the matches to extract key-value pairs, and adds them to the dictionary. The keys and values are converted to lowercase for consistency.

### /app/data_processing/db_handler/

The `db_handler` module is responsible for interacting with the database. It handles tasks such as establishing a connection to the database, executing queries, fetching results, and closing the connection. This module is crucial for storing and retrieving the data processed by the application.

### /app/data_processing/db_handler/query_history.py

The `query_history` file checks if a query already exists in a certain time range (default is 24 hours). If it exists, it returns it and if not, it creates a new one by calling the `ssh_prompt_handler` module to obtain the ONT dictionaries and creates a JSON where it stores the date and time of the query and the OLT and ONT data. Then, it saves this JSON in the database and returns the query to be displayed on the web page.

### /app/data_processing/error_handler/

The `error_handler` module is responsible for managing and handling errors that occur within the application. It handles tasks such as logging errors, sending error notifications, and possibly providing recovery strategies.

### /app/data_processing/error_handler/errors.py

The `errors.py` file defines a custom exception class, `personalized_exception`, and a function, `error_return`, for raising this exception. The `personalized_exception` class inherits from the built-in `Exception` class and adds two attributes: `human_readable` and `technical_error`. These attributes are used to store human-readable and technical error messages, respectively. The `__str__` method of the class returns a formatted string representation of the exception. The `error_return` function takes two arguments, a human-readable error message and a technical error message, and raises a `personalized_exception` with these messages. This file is used to handle errors in a personalized way throughout the application.

### /app/data_processing/error_handler/user_input.py

The `user_input.py` file is responsible for validating and processing user inputs. It contains functions to validate IPv4 addresses and serial numbers, ensuring they meet specific conditions such as length, base, and character requirements. It also includes a function to retrieve input from command line arguments and perform the necessary validation. If the expected arguments are not provided, a custom error is raised. This file is essential for handling user input in a secure and structured manner.

### /app/database

The `database` module takes care of all tasks directly related to the database. In this case it is only responsible for establishing the connection to the database.

### /app/database/connection.py

The `connection.py` file is responsible for managing the MongoDB connection for the application. It defines a singleton class, `MongoConnection`, which ensures that only one instance of the MongoDB connection exists throughout the application. This class includes methods to initialize the PyMongo instance, initialize it with a Flask app, and retrieve the database and 'queries' collection from the instance. The `init_db` function is defined outside the class to initialize the database with a Flask app. This file is crucial for ensuring efficient and consistent database operations in the application.

### /app/static

The `static` module servs the static files in the application. These files could include CSS, JavaScript, images, and other assets that are not dynamically generated. This module is crucial for providing the necessary resources for the client-side rendering of the application.

### /app/static/css; /app/static/img and /app/static/js

The `css` directory contains Cascading Style Sheets (CSS) files that style the HTML elements of the web application, the `img` directory stores image files used in the application, such as icons and background images, and the `js` directory contains JavaScript files that add interactivity to the web pages.

### /app/templates

The `templates` module contains the HTML templates that define the structure and layout of the web pages in the application. These templates can be dynamically rendered with data by the application, allowing for user-specific views and content.

### /app/templates/base.html

The `base.html` file is a base template for the web application. It sets up the basic HTML structure, including the `DOCTYPE`, `html`, `head`, and `body` tags. Inside the `head` tag, it defines meta tags for character set and viewport, a title block that can be overridden by child templates, and links to CSS stylesheets. The `body` tag contains a header with a logo, title, and a help link. The body of the page is defined by a `block` tag that can be filled in by child templates. This base template provides a consistent layout and style for all pages in the application, while allowing flexibility for individual pages to define their own content.  
The Jinja2 engine is what allows you to make templates with inheritance.

### /app/templates/index.html

The `index.html` file is a template for the main page of the web application. It extends the base template, `base.html`, and defines the content for the `title` and `body` blocks. The body contains a form for users to enter an OLT IP and an ONT SN, which are then sent to the `/buscar` route on form submission. There's also a section to display error messages and an image. The form includes a button for submitting the form, and a message that is displayed while the request is being processed. The results of the request are displayed in a `div` element with the id `result`. At the end of the file, a JavaScript file, `index_app.js`, is linked to add interactivity to the page.

### /app/templates/help.html

The `help.html` file is a template for the help page of the web application. It extends the base template, `base.html`, and defines the content for the `title` and `body` blocks. The body contains several sections with information on how to use the application, including a basic guide, usage instructions, a technical guide, and information on what to do in case of technical problems. Each section is marked with an `h2` tag for the title and a `p` or `ol` tag for the content. The technical guide section includes a link to the project on GitHub for more technical information. This template provides helpful information to users on how to use the application.

### /app/templates/results.html

The `results.html` file is a template for the results page of the web application. It extends the base template, `base.html`, and defines the content for the `title` and `body` blocks. The body contains a section with a table that displays the results of a query. The table includes the OLT IP, ONT SN, date and time of the query, and key-value pairs from the query result. There's also a form to submit a new request to refresh the data, and a button to show more information. At the end of the file, a JavaScript file, `results_app.js`, is linked to add interactivity to the page. This template presents the query results in a user-friendly format.
