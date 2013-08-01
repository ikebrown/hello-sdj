hello-sdj
=========

Hello SDJournal.org


Get Started with Django
=======================

Follow the docs at https://docs.djangoproject.com/en/dev/intro/tutorial01/

%> django-admin.py startproject django_sdj  
%> cd django_sdj  
%> python manage.py runserver  
Go to http://localhost:8000 in your browser


Add sqlite3 database for simplicity in settings.py:

        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_sdj.sqlite3',

%> python manage.py syncdb      # run through the prompts
