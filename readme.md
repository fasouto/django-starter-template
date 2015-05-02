# django-starter-template #

An opinionated but easy to use project template for Django 1.8

## Features ##

- [Django compressor](http://django-compressor.readthedocs.org/en/latest/) to compress JS and CSS and compile LESS/SASS files.
- [Django debug toolbar](http://django-debug-toolbar.readthedocs.org/) enabled for admins.
- [Bcrypt](https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#using-bcrypt-with-django) to hash the passwords
- Ready to push to Heroku
- [Django flat theme](https://github.com/elky/django-flat-theme) to style the admin.

## Usage ##

First create and activate your virtualenv, you can use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/). Then install Django 1.8 in your virtualenv:

    pip install django==1.8

To create a new Django project

    django-admin.py startproject --template=https://github.com/fasouto/django-starter-template/archive/master.zip --extension=py,md,html,txt project_name

And finally to install the dependencies

    pip install -r requirements/development.txt

If you need a database, edit the settings file and create one with
   
    python manage.py syncdb

Once everything is setup to run the development server in http://localhost:8000/

    python manage.py runserver
