<h1 align="center">REST API Project - SOFTDESK - OpenClassRooms Project 10</h1>
<br>
<br>
Ce script Python est le 10e projet réalisé dans le cadre d'une formation chez OpenClassrooms.
<br>

## OVERVIEW
Beta version of a RESTful API made with Django REST Framework. SoftDesk is an API for managing to-do lists  (issue tracking system).This solution is aimed at corporate customers, in B2B.<br>
The app will basically allow users to create various projects, add contributors to specific projects, create issues within projects and assign labels to those issues based on their priorities, tags, etc. <br> 
The access is granted to authenticated users via JSON Web Tokens (JWTs).

## REQUISITORIES
Python 3 <br>
Django 3 <br>
Django REST Framework 3 <br>
<br>

## INSTALLATION
Start by closing the repository :
```
git clone https://github.com/pascaline841/api-tracking-system
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
## . . . 
Install the python dependencies to the virtual environment
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
python manage.py createsuperuser
```
Create and open a file named .env then paste :
```
SECRET_KEY= 
```
Then complete DB_SECRET_KEY with the key you receive in private.

## EXECUTION
Run the program
```
python manage.py runserver
```
Launch 
```
http://127.0.0.1:8000
```
To access to the admin account 
```
http://127.0.0.1:8000/admin
```
To create an user account (different to admin account) 
```
http://127.0.0.1:8000/signin
```
To log in and obtain JSON Web Token 
```
http://127.0.0.1:8000/login
```
## Test the API with POSTMAN
A Public Postman collection is available to test the API endpoints.
```
https://documenter.getpostman.com/view/16100693/TzeXk7Qo
```
## USER TESTS with a PRESET DATABASE
If you would like to test the API, there is a preset database with 1 admin and 3 users.
```
python manage.py migrate
```
```
python manage.py loaddata fixtures/dumb.json
```
Then, run the program. <br>
LOGIN : admin (john, jane, pasca) <br>
PASSWORD : OCPython2021 <br>
