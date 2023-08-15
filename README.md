## Install:
-git
-Python version 3.8 
-PostgreSQL version 15.3
-pgAdmin
-node v16.19.1

## Basic Settings for Development

    # Create a new database(postgresql)

CREATE DATABASE 'your_dbname'

   #Activate environment

windows:    python -m venv venv
Unix/MacOS: python3 -m venv venv

   #Open environment

windows:    venv\Scripts\activate.bat
Unix/MacOS: source venv/bin/activate

## Install Library

- pip3 install django
- pip3 install django-environ
- pip3 install psycopg2-binary
- pip3 install opencv-python
- pip3 install matplotlib


You’ll have to make the following creations to your your .env file
and Django Secret Key

    DB_NAME=your_database_name
    DB_USER=your_user_name
    DB_PASS=your_password

    SECRET_KEY='your_secret_key'

## Install dependencies
   windows:   pip install -r requirement-dev.txt
   Unix/MacOS:   pip3 install -r requirement-dev.txt

## Add freeze
   
   windows:   pip freeze > req_name.txt
   Unix/MacOS:   pip3 freeze > req_name.txt


## Make migrations and Apply to database
    python manage.py makemigrations 
    python manage.py migrate
## Setup Initial User, and Admin

    # create first user
    python manage.py createsuperuser

## Run project

python manage.py runserver 

## Go to
    localhost:8000/admin/