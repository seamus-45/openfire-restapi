# -*- coding: utf-8 -*-

VERSION = (0, 1)

from users import Users
from muc import Muc
from system import System
from groups import Groups
from sessions import Sessions
from messages import Messages


def get_version():
    version = '{0}.{1}'.format(VERSION[0], VERSION[1])
    return version
