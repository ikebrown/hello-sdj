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
Go to http://localhost:8000 in your browser to check it's not broken


%> python manage.py startapp hello    # generates hello directory  
You edit settings.py according to django instructions to add your app  
See: https://github.com/mdagosta/hello-sdj/commit/c8970ded6fc015f57278ad128f5b9195eeaa2a4e

%> python manage.py sql hello  # sample output. if it looks ok...  
%> python manage.py syncdb

Django's docs for part 2 are great and I don't have anything to add... skipping the admin stuff






