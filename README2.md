# Optical Network Terminal Information

### Obtains and displays useful information about the status and operation of a specific ONT

This project consists of a web application that is responsible for retrieving data from the requested ONT through an SSH connection to the OLT that makes the request. Then, save that query in the database so that the next time a new similar one is made within a certain time range, the website will use the already created query to be displayed.

The goal is to automate the process of searching and obtaining all relevant information from a customer's ONT.

![](app/static/img/functionality-explained.png)
*A simple diagram showing the entire process of collecting and displaying the ONT information.*

## 📟 Supported OLT Models

- [X] [Huawei SmartAX MA5800-X2](https://support.huawei.com/enterprise/en/optical-access/smartax-ma5800-pid-21484577)

## 🔧 Technologies Used

### Backend
- **Flask**: A micro web framework for Python used to create the web application.
- **Python**: The primary programming language for server-side logic and data processing.

### Database
- **MongoDB**: A NoSQL database used to store and manage data for the application.

### Frontend
- **HTML**: Used for creating the structure and content of web pages.
- **CSS**: Used for styling the web pages to improve the user interface.
- **JavaScript**: Implemented for enhancing interactivity and functionality on the client-side.

### Additional Tools and Libraries
- **[pexpect](https://pexpect.readthedocs.io/en/stable/)**: Used for automating interactions with command-line applications.
