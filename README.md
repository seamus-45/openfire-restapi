openfire-restapi
================

A python client for Openfire's REST API Plugin

Requirements
----------------
* python-setuptools
* python-requests
* python-virtualenv (optional)


Installation
----------------

Install from source:

        $ git clone git://github.com/seamus-45/openfire-restapi.git
        $ cd openfire-restapi
        $ sudo python setup.py install
        
Also, you can install this package in python virtual environment:

        $ python2.7 -m virtualenv env
        $ source env/bin/activate
        $ pip install requests
        $ git clone git://github.com/seamus-45/openfire-restapi.git
        $ cd openfire-restapi
        $ pip install .

Documentation
----------------
* [User related](docs/users.md)
* [Groups related](docs/groups.md)
* [Chat room related](docs/muc.md)
* [Session related](docs/sessions.md)
* [Messages related](docs/messages.md)
* [System related](docs/system.md)
