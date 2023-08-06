## Basic Settings for Development

   #Activate environment

windows:    python -m venv venv
Unix/MacOS: source venv/bin/activate 

   #Open environment

windows:    venv\Scripts\activate.bat
Unix/MacOS: source venv/bin/activate

## Install dependencies
    pip install -r requirements.txt

## Setup Initial User, and Admin

    # create first user
    python manage.py createsuperuser

## Run project

python manage.py runserver 