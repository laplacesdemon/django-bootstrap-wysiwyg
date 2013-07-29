This sample django project demonstrates the usage of `django-bootstrap-wysiwyg` app.

Installation
------------

Install virtualenv if it's not installed before

    pip install virtualenv

Use following to set up the project

    virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements.txt 

Then run it

    python manage.py syncdb
    python manage.py runserver

Dependencies
------------

see requirements.txt

There are some django apps that I use for the sample application. These dependencies are
only required for the sample project. To see the `django-bootstrap-wysiwyg` dependencies
please see `../requirements.txt`
