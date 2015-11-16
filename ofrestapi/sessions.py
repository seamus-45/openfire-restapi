# -*- coding: utf-8 -*-
from requests import (get, delete)
from base import Base


class Sessions(Base):

    def __init__(self, host, secret, endpoint='/plugins/restapi/v1/sessions'):
        """
        :param host: Scheme://Host/ for API requests
        :param secret: Shared secret key for API requests
        :param endpoint: Endpoint for API requests
        """
        super(Sessions, self).__init__(host, secret, endpoint)

    def get_sessions(self):
        """
        Retrieve sessions of all users
        """
        return self._submit_request(get, self.endpoint)

    def get_user_sessions(self, username):
        """
        Retrieve sessions of exact user

        :param username: The user name
        """
        endpoint = '/'.join([self.endpoint, username])
        return self._submit_request(get, endpoint)

    def close_user_sessions(self, username):
        """
        Close sessions of exact user

        :param username: The user name
        """
        endpoint = '/'.join([self.endpoint, username])
        return self._submit_request(delete, endpoint)
