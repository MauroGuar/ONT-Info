# ONT-Info
## Description
ONT-Info is a web app designed to retrieve info from an OLT about a ONT in question through SSH.
### supported olt's models:
* Huawei SmartAX MA5800-X2

### Technologies used:

ONT-Info is almost entirely made on python:
* pymongo for the db-connection.
* flask for the back-end.
* pexpect for ssh-connection and commands.

The database is Mongo-DB, and the front end is a static page made with html and css

### Showcase:

## Installation:

### system Installation (deprecated)

#### Requirements:

* a mongoDB URI (which you get from a mongoDB running server, either in the cloud or locally, go see MongoDB docs)
* Python3
* pip
* git
* a way of editing and executing files

#### Install steps:

Clone the project wherever you like:

`git clone https://github.com/MauroGuar/ONT-Info.git `

Enter the project directory:

`cd ./ONT-info`

Install pexpect

`python -m pip install pexpect`

Install pymongo

`python -m pip install pymongo`

Inside the repo you just cloned , copy the file `.env.example` to `.env`

`cp ./.env.example ./.env`

Edit the `.env` file:

`nano ./.env`

you should see something like the following

```
# Default variables
OLT_USERNAME=
OLT_PASSWORD=


# Test variables
OLT_IP=
ONT_SN=

MONGO_URI=
```
Now, fill in each field with the necessary data

When you filled each field accordingly, press `CTRL + X` , the following text should be prompted on the down left corner saying the following:
`Save modified buffer?`

Press the letter `Y` as in Yes.

##### Run the program

`python ./run.py`

### Docker

[Install Docker](https://docs.docker.com/get-docker/)

[Install Docker compose](https://docs.docker.com/compose/install/) (If needed, some docker installations already come with it)

Clone the project wherever you like:

`git clone https://github.com/MauroGuar/ONT-Info.git `

Enter the project directory:

`cd ./ONT-info`

Inside the repo you just cloned , copy the file `.env.example` to `.env`

`cp ./.env.example ./.env`

Edit the `.env` file:

`nano ./.env`

you should see something like the following

```
# Default variables
OLT_USERNAME=
OLT_PASSWORD=


# Test variables
OLT_IP=
ONT_SN=

MONGO_URI= mongodb://mongo:27017/mydatabase
```
Now, fill in each field with the necessary data

When you filled each field accordingly, press `CTRL + X` , the following text should be prompted on the down left corner saying the following:
`Save modified buffer?`

Press the letter `Y` as in Yes.

##### Run the program

`sudo docker compose up --build -d`

Now you should be able of entering the program entering http://127.0.0.1/ on your web browser on the host pc or your local ip address, remember that this service uses the port 80.

## FAQ

### I do not see my OLT model, what should i do?

You should test the program, and open an issue saying if it works or not, in that case, also paste the errors.

### How to contribute?

See contributing.md inside /docs/

### How is the code structured? 

See program-structure.md inside /docs/
