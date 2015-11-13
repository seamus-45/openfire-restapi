# -*- coding: utf-8 -*-


class IllegalArgumentException(Exception):
    pass


class UserNotFoundException(Exception):
    pass


class UserAlreadyExistsException(Exception):
    pass


class RequestNotAuthorisedException(Exception):
    pass


class UserServiceDisabledException(Exception):
    pass


class SharedGroupException(Exception):
    pass


class InvalidResponseException(Exception):
    pass


class PropertyNotFoundException(Exception):
    pass


class GroupAlreadyExistsException(Exception):
    pass
