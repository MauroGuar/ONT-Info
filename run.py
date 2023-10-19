# Import the 'app' object from the 'main' module
from app.main import app

# Check if the script is being run as the main program
if __name__ == "__main__":
    # If the script is the main program, execute the following:

    # Start the Flask web application defined in the 'app' object
    app.run(debug=True)

# Explanation:
# This code is found at the end of a Python script that uses the Flask web framework. It serves two main purposes:

# 1. Importing the Flask application instance ('app'):
#    - It imports the 'app' object from the 'main' module, which is where the Flask application is defined.
#    - The 'app' object is responsible for configuring and running the Flask web application.

# 2. Conditional block for running the Flask application:
#    - The code checks whether the script is being executed as the main program (rather than being imported as a module).
#    - If the script is indeed the main program, the 'if __name__ == "__main__":' block is executed.
#    - Inside the block, the Flask application is started with the 'app.run()' method.
#    - The 'debug=True' argument is provided to enable debugging mode, which is useful for development and debugging purposes.

# The result is that when you run this Python script directly, it starts the Flask web application and listens for incoming HTTP requests. This is a common way to start a Flask application for local development and testing.
