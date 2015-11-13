# -*- coding: utf-8 -*-
from exception import (IllegalArgumentException, UserNotFoundException, UserAlreadyExistsException,
                       RequestNotAuthorisedException, UserServiceDisabledException,
                       SharedGroupException, InvalidResponseException, PropertyNotFoundException,
                       GroupAlreadyExistsException)


EXCEPTIONS_MAP = {
    'IllegalArgumentException': IllegalArgumentException,
    'UserNotFoundException': UserNotFoundException,
    'UserAlreadyExistsException': UserAlreadyExistsException,
    'RequestNotAuthorised': RequestNotAuthorisedException,
    'UserServiceDisabled': UserServiceDisabledException,
    'SharedGroupException': SharedGroupException,
    'PropertyNotFoundException': PropertyNotFoundException,
    'GroupAlreadyExistsException': GroupAlreadyExistsException,
}


class Base(object):

    def __init__(self, host, secret, endpoint):
        """
        :param host: Scheme://Host/ for API requests
        :param secret: Shared secret key for API request
        :param endpoint: Endpoint for API request
        """
        self.headers = {}
        self.headers['Authorization'] = secret
        self.headers['Accept'] = 'application/json'
        self.host = host
        self.endpoint = endpoint

    def _submit_request(self, func, endpoint, **kwargs):
        """
        Wrapper for send a request

        :param func: Name of the function for request
        :param endpoint: Plugin endpoint for request
        :param **kwargs: Arguments that request takes
        :return: JSON object or True
        """
        r = func(
            headers=self.headers,
            url=self.host + endpoint,
            **kwargs
        )
        if r.status_code in (200, 201):
            try:
                return r.json()
            except:
                return True
        else:
            try:
                exception = r.json()['exception']
                message = r.json()['message']
            except:
                raise InvalidResponseException(r.status_code)
            if exception in EXCEPTIONS_MAP:
                raise EXCEPTIONS_MAP[exception](message)
            else:
                raise InvalidResponseException(exception)
