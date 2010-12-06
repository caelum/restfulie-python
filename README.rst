Restfulie Python
================

Restfulie python port is in earlier stages. Wait a while for some extra information and docs.

Meanwhile visit `Restfulie's website <http://restfulie.caelumobjects.com>`_.

How to install
--------------

You need some native dependencies for the lxml library. On Ubuntu, you must run::

  apt-get install libxml2 libxslt1.1 libxslt1-dev


Makefile installs the dependencies using `Pip <http://pip.openplans.org/>`_, then you have to install it (run with root privileges)::

  apt-get install python-setuptools

  easy_install pip


After install these system-related dependencies, you can run `make` to install all Python dependencies (if they are not installed) and run all tests. Depending on your environment, this script may need root permissions in order to install the dependencies.


A simple get
------------

A simple post
-------------

How to contribute
-----------------

The Restfulie python is an open source project. To contribute, just fork the `central repository <http://github.com/caelum/restfulie-python>`_, make your changes and send a pull request (please, send a expressive message.)

The principal issues to resolve in `restfulie python are in here <http://restfulie.lighthouseapp.com/projects/53571-restfulie-python>`_.

License
-------

Restfulie is licensed under the Apache License, Version 2.0.

