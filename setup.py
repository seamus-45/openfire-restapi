# -*- coding: utf-8 -*-

from setuptools import setup

from ofrestapi import __version__


setup(
    name='openfire-restapi',
    version=__version__,
    description=u'A python client for Openfire’s REST API Plugin',
    license="GPL-3",
    author='Sergey Fedotov (seamus-45)',
    author_email='sr.fido@gmail.com',
    url='https://github.com/seamus-45/openfire-restapi',
    packages=['ofrestapi']
)
