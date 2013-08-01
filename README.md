hello-sdj
=========

Hello SDJournal.org


Get Started with Django
=======================

Follow the docs at https://docs.djangoproject.com/en/dev/intro/tutorial01/

The Django docs walk you through something of a Minimum Viable Server, complete with error handlers and forward-thinking practices. I'll walk you through setting up a Minimum Functioning Program that just barely gets off the ground and has a feature.

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

Django's docs for part 2 on the Admin Interface are great so I don't have much to add... for what it's worth here's what I needed to enable Admin:

https://github.com/mdagosta/hello-sdj/commit/7e4744e7c92be1e3430a147b4965ae0b7172dd03


Creating a view:
================

Start by editing urls and views: https://github.com/mdagosta/hello-sdj/commit/a1882138363ff684c11b427a37a067a75166cff1


Create a feature:
=================

Commits are worth a thousand words each:

https://github.com/mdagosta/hello-sdj/commit/866c88b3d51724f5e1a8177ce56d66565dc3e8bb

https://github.com/mdagosta/hello-sdj/commit/b97230fbc08ea85c8c8730609f32c3befc097314
