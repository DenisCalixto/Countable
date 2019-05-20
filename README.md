# Countable - Clark's Test

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

- open a terminal, navigate to the project folder and create a virtual environment. I.e.: 'virtualenv myenv'

- in the terminal, activate the virtual environment. 

Linux or Mac: source /PATHTOENV/bin/activate
Windows: c:\PATHTOENV\Scripts\activate

- in the terminal, install django version 2.0.2: 'pip install django==2.0.2'

- in the terminal, install mysqlclient: 'pip install mysqlclient'

- in the terminal, install Pillow (for the images): 'pip install Pillow'

- in settings.py, change the current database configurations according to your environment:

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

- run django server

- you are good to go!