# django-starter-template #

A project template for Django 1.8

## Usage ##

First you need to create a working environment with [virtualenv](http://www.virtualenv.org/).

    $ virtualenv my_venv

And then activate it:

    $ source my_venv/bin/activate

You'll need to activate your virtualenv every time you want to run the project. To install Django in the new virtualenvironment

    $ pip install django==1.8

To create a new Django project

    $ django-admin.py startproject --template=https://github.com/fasouto/django-starter-template/archive/master.zip --extension=py,md,html,txt project_name

And finally to install the dependencies

    $ pip install -r requirements/development.txt

If you need a database, edit the settings file and create one with
   
    $ pip manage.py syncdb

Once everything is setup to run the development server in http://localhost:8000/

    $ python manage.py runserver

## Why? ##
This project template was created in order to be simple and make development faster for my clients. It follows django best practices. There are other django project templates:

 - https://github.com/twoscoops/django-twoscoops-project
 - https://github.com/xenith/django-base-template
 - https://github.com/nigma/django-modern-template
 - https://github.com/amccloud/django-project-skel