# Countable - Pictionary Game

Software required:

- MySQL (does not need to be the lastest version but avoid very old ones).
- Pip3
- Python3
- Virtualenv
- Git
- a code editor of your choosing

Instructions:

- create a database on your local MySQL server.

- clone git repository:
https://github.com/DenisCalixto/Countable.git

- open a terminal, navigate to the root folder of the project (Readme file level) and create a virtual environment. I.e.: 'virtualenv myenv'

- in the terminal, activate the virtual environment. 

Linux or Mac: source /PATHTOENV/bin/activate

Windows: c:\PATHTOENV\Scripts\activate.bat

- install django version 2.0.2: 'pip install django==2.0.2'

- install mysqlclient: 'pip install mysqlclient'

- install Pillow (for the images): 'pip install Pillow'

- navigate to folder countabletest-project

- open the file countabletest-project\countabletest\settings.py and change the database configurations according to your environment:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOUR_DATA_BASE_NAME',
        'USER': 'DATABASE_USER',
        'PASSWORD': 'DATABASE_USER_PASSWORD',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

- in the terminal, navigate to the folder countabletest-project and run the migrations: python manage.py migrate

- run django server: python manage.py runserver

- open url http://127.0.0.1:8000 in your browser and you are good to go!
