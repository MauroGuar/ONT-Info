# Program Structure

The structure of the program is mainly made based on Flask's structuring standards, with some personal modifications.  
The project is divided into two large sections, the project path "/" and the "app/" directory.  
In the main directory, there are the files for the execution and explanation of the program.  
In the app directory you will find the files and modules with the code necessary for the program to function.

## Inside /app/

### /app/main.py

The `main.py` file is the main entry point of the Flask web application. It sets up the Flask application, configures and initializes a MongoDB database connection, and defines routes for handling different URLs. Each route is associated with a function that processes data and returns a response to the client. The functions handle tasks such as rendering HTML templates, processing form data, storing results in session variables, and redirecting to other routes.

### /app/config.py

The `config.py` file is responsible for managing the configuration of your application. It finds and loads the `.env` file from your project directory. This file contains environment variables that are used throughout your application. The `config.py` file retrieves these variables.

### /app/.env and /app/.env.example

The `.env` and `.env.example` files are used to store environment variables for your application. These variables include `OLT_USERNAME` and `OLT_PASSWORD` for SSH connection credentials to an OLT device, `MONGO_URI` for the MongoDB connection URI, and `FLASK_SESSION_SECRET_KEY` for the secret key used in Flask sessions. The `.env.example` file serves as a template, while the actual values are stored in the `.env` file. The values are kept empty in the `.env.example` file for security reasons, and actual values should be filled in the `.env` file on your local machine.  
It is important to add that the `.env` file is ignored by git in the `.gitignore` file, so the secret credentials are not published.

### /app/data_processing/

The `data_processing` module is responsible for collecting, processing, and returning data from the entire application.  

### /app/data_processing/ont_info.py

The `ont_info.py` file is like the "main" of the entire data_processing module because it calls and uses all functions of the rest of the internal data processing modules in order.  
It contains functions for handling and processing data related to Optical Line Terminal (OLT) and Optical Network Terminal (ONT) devices. It includes functions to format time, convert query results into a user-friendly format, refresh queries by creating new ones for specific OLT IP and ONT serial numbers, and make new requests for specific OLT IP and ONT serial numbers. These functions are used to manage and process data from the OLT and ONT devices, handle queries related to these devices, and present the data in a suitable format.

### /app/data_processing/ssh_prompt_handler/

The `ssh_prompt_handler` module is responsible for establishing the ssh connection with the OLT, collecting and validating the ONT data and transforming it into dictionary format.

### /app/data_processing/ssh_prompt_handler/dictionary_converter.py

