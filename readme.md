# django-starter-template #

An opinionated but easy to use project template for Django 1.8

## Features ##

- [Django compressor](http://django-compressor.readthedocs.org/en/latest/) to compress JS and CSS and compile LESS/SASS files.
- [Django debug toolbar](http://django-debug-toolbar.readthedocs.org/) enabled for admins.
- [Bcrypt](https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#using-bcrypt-with-django) to hash the passwords
- [Django flat theme](https://github.com/elky/django-flat-theme) to style the admin.

## Quickstart ##

First create and activate your virtualenv, you can use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/). Then install Django 1.8 in your virtualenv:

    pip install django==1.8

To create a new Django project (make sure to change `project_name`)

    django-admin.py startproject --template=https://github.com/fasouto/django-starter-template/archive/master.zip --extension=py,md,html,txt project_name

cd to your project and install the dependences

    pip install -r requirements/development.txt

If you need a database, edit the settings and create one with
   
    python manage.py syncdb
    python manage.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python manage.py runserver

## How to use it ##

### Settings ###

Settings are divided by environments: production.py, development.py and testing.py. By default it uses development.py, if you want to change the environment set a environment variable:

    export DJANGO_SETTINGS_MODULE=“my_project.settings.production”

or you can use the `settings` param with runserver:

    python manage.py runserver --settings=my_project.settings.production


If you need to add some settings that are specific for your machine, rename the file `local_example.py` to `local.py`. This file it's in .gitignore so the changes won't be tracked.

### Bootstrap ###

[Bootstrap 3](http://getbootstrap.com/css/#less) LESS files are included and compiled with django_compressor. There's an extra file `app.less` where you should put your CSS instead of override bootstrap LESS files, so you can update bootstrap easily.
