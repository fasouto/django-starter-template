# django-starter-template #

An easy to use project template for Django 1.10 that follows best practices.

## Features ##

- Compatible with python 2.7 and 3.4
- [Django compressor](http://django-compressor.readthedocs.org/en/latest/) to compress JS and CSS and compile LESS/SASS files.
- [Django debug toolbar](http://django-debug-toolbar.readthedocs.org/) enabled for superusers.
- [Argon2](https://docs.djangoproject.com/en/1.10/topics/auth/passwords/#using-argon2-with-django) to hash the passwords
- A [fabfile](http://www.fabfile.org/) to ease the deployment.

## Quickstart ##

First create and activate your virtualenv, you can use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/). Then install Django 1.10 in your virtualenv:

    pip install django==1.10

To create a new Django project (make sure to change `project_name`)

    django-admin.py startproject --template=https://github.com/fasouto/django-starter-template/archive/master.zip --extension=py,md,html,txt,less project_name

cd to your project and install the dependences

    pip install -r requirements.txt

If you need a database, edit the settings and create one with
   
    python manage.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python manage.py runserver

## How to use it ##

### Settings ###

Settings are divided by environments: production.py, development.py and testing.py. By default it uses development.py, if you want to change the environment set a environment variable:

    export DJANGO_SETTINGS_MODULE="my_project.settings.production"

or you can use the `settings` param with runserver:

    python manage.py runserver --settings=my_project.settings.production

If you need to add some settings that are specific for your machine, rename the file `local_example.py` to `local_settings.py`. This file it's in .gitignore so the changes won't be tracked.

### Bootstrap ###

[Bootstrap 3](http://getbootstrap.com/css/#less) LESS files are included and compiled with django_compressor. There's an  file `less/app.less` where you should put your CSS to avoid overriding the bootstrap LESS files, so you can update bootstrap easily.

Make sure you have [lessc](http://lesscss.org/#using-less-installation) installed on your production server, for development it uses less.js.

### Dependencies ###

We are following [Kenneth Reitz's pip workflow](http://www.kennethreitz.org/essays/a-better-pip-workflow) to handle [requirements files](https://pip.readthedocs.org/en/1.1/requirements.html). The `requirements_to_freeze.txt` contains unpinned requirements and `requirements.txt` contains the pinned versions to use in a deployment.

If you have trouble/can't install a package place it in the `/libs` directory.


### TODO ###
 - Add webpack with live SASS reloading.
 - Once we have webpack upgrade to bootstrap 4
 - Add gitlab.ci
 - Improve tox.ini
 - Improve deployment, get rid of fabric. Investigate feasible options. Maybe add a deploy to heroku/docker cloud.
 - Add some example code and tests.
