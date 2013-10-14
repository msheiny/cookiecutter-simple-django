from .base import *


ADMINS = (
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS

DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.{{cookiecutter.db_backend}}',
        'NAME': '{{cookiecutter.db_name}}',
        'USER': '{{cookiecutter.db_user}}',
        'PASSWORD': '{{cookiecutter.db_password}}',
        'HOST': '{{cookiecutter.db_host}}', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }   
}

# You might want to use sqlite3 for testing in local as it's much faster.
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/{{cookiecutter.repo_name}}_test.db',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
