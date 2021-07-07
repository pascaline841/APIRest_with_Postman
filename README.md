<h1 align="center">DJANGO Project - SOFTDESK - OpenClassRooms Project 10</h1>
<br>
<br>
Ce script Python est le 10e projet réalisé dans le cadre d'une formation chez OpenClassrooms.
<br>

## OVERVIEW
Beta version of a RESTful API made with Django REST Framework.SoftDesk is an API for managing to-do lists within IT Teams. <br>
Allows you to create a project with issues and comments. The access is granted to authenticated users via JSON Web Tokens (JWTs). Only contributors can access the details of a project. Only authors or managers can update or delete.
<br>
## REQUISITORIES
Python 3 <br>
Django 3 <br>
Django REST Framework 3 <br>
<br>

## INSTALLATION
Start by closing the repository :
```
git clone https://github.com/pascaline841/p10
```
Start access the project folder

## for Window
Create a virtual environment
```
python -m venv env
```
Enable the virtual environment
```
cd env/scripts
source activate
```

## for Linux or macOS
Create a virtual environment 
```
python3 -m venv env
```
Activate the virtual environment with 
```
source env/bin/activate 
```
<br>
## for Window, Linux or macOS
Install the python dependencies on the virtual environment
```
pip install -r requirements.txt
```
Create the database structure by using sqlite3
```
python manage.py migrate
```
Create an administrative account :<br>
You will be asked to select a username, provide an email address, and choose and confirm a password for the account.
```
winpty python manage.py createsuperuser
```
Create and open a file named .env then paste :
```
DB_SECRET_KEY= 
```
Then complete DB_SECRET_KEY with the key you receive in private.

## EXECUTION
Run the program
```
python manage.py runserver
```
Launch :
```
http://127.0.0.1:8000
```
To access to the admin account :
```
http://127.0.0.1:8000/admin
```

## API use with POSTMAN
Endpoints can be tested with tools such as Postman or cURL.<br>
A Public Postman collection is available to test the API endpoints.
```
adress
```
## Use FLAKE8
In order to generate a flake8 report, run the following command :
```
flake8 --ignore=E501,W503 --format=html --htmldir=flake-report --exclude=venv,manage.py,db.sqlite3,litreview
```
Open the html file into the flake-report repertory to show the report.
