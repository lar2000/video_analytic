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
Unix/MacOS: source venv/bin/activate 

   #Open environment

windows:    venv\Scripts\activate.bat
Unix/MacOS: source venv/bin/activate

## Install dependencies
    pip install -r requirements.txt

## Basic Settings

You’ll have to make the following creations to your your .env file
and Django Secret Key

    DB_NAME=your_database_name
    DB_USER=your_user_name
    DB_PWD=your_password

    SECRET_KEY='your_secret_key'
# Basic Settings(open setting.py in your project)

Below your import in settings.py:

import environ
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env("SECRET_KEY")
.
.
.

"ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASS"),
        "HOST": "127.0.0.1",

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