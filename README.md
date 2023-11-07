# Django-Boilerplate
This is a boilerplate intended for creating a REST API with Python Django


## STEPS TO GET STARTED WITH THIS BOILERPLATE
1. Create a local_settings.py file that contains your database settings and secret key in the following format:
    <code>
    SECRET_KEY = "***********************"
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '3306',
            'OPTION': {
                'autocommit': True
            }
        }
    }
    </code>
2. Open the terminal and run the following commands:
    - pipenv install 
    - pipenv shell
3. Connect your environment to your project. To get your environment name run the following command:
    - pipenv -venv
4. Copy the text after the pipenv -venv command
5. Open the Command Palette select the Python Interpreter. Add a new one and paste the copied text to connect your environment
6. Run the following commands to make your initial migration to your database
    - python manage.py makemigrations
    - python manage.py migrate
6. Use the movie sample app as reference to create endpoints, functions and serializers. 