# Create a new database(postgresql)

CREATE DATABASE 'your_dbname'

## Basic Settings for Development

   #Activate environment

windows:    python -m venv venv
Unix/MacOS: source venv/bin/activate 

   #Open environment

windows:    venv\Scripts\activate.bat
Unix/MacOS: source venv/bin/activate

## Install dependencies
    pip install -r requirements.txt

# Basic Settings(open setting.py in your project)
"ENGINE": "django.db.backends.postgresql",
        "NAME": "your_dbname",
        "USER": "your_username",
        "PASSWORD": "your password",
        "HOST": "127.0.0.1",
        "PORT": "5432", 

## Make migrations and Apply to database
    python manage.py makemigrations 
    python manage.py migrate
## Setup Initial User, and Admin

    # create first user
    python manage.py createsuperuser

## Run project

python manage.py runserver 