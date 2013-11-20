
cookiecutter-django
=======================

A cookiecutter_ template for Django.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Description
-----------

Originally forked from marcofucci_ with minimal changes

.. _marcofucci: https://github.com/marcofucci/cookiecutter-simple-django

Tweaked it a bit for my needs, added additional cookiecutter attributes, 
trimmed read-me.

Usage
------

Now run it against this repo::

    $ cd <your-workspace>
    $ cookiecutter  https://github.com/msheiny/cookiecutter-simple-django.git

You'll be prompted for some questions, answer them, then it will create a Django 
skeleton project for you.

Notes
-----

* Put secret key inside the virtual environment bin/postactivate script

    export SECRET_KEY="blah"

