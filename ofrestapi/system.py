# -*- coding: utf-8 -*-
from requests import (get, post, delete)
from base import Base


class System(Base):

    def __init__(self, host, secret, endpoint='/plugins/restapi/v1/system/properties'):
        """
        :param host: Scheme://Host/ for API requests
        :param secret: Shared secret key for API requests
        :param endpoint: Endpoint for API requests
        """
        super(System, self).__init__(host, secret, endpoint)

    def get_props(self):
        """
        Retrieve all system properties
        """
        return self._submit_request(get, self.endpoint)

    def get_prop(self, key):
        """
        Retrieve system property

        :param key: The name of system property
        """
        endpoint = '/'.join([self.endpoint, key])
        return self._submit_request(get, endpoint)

    def update_prop(self, key, value):
        """
        Create or update a system property

        :param key: The name of system property
        :param value: The value of system property
        """
        payload = {
            '@key': key,
            '@value': value,
        }
        return self._submit_request(post, self.endpoint, json=payload)

    def delete_prop(self, key):
        """
        Delete a system property

        :param key: The name of system property
        """
        endpoint = '/'.join([self.endpoint, key])
        return self._submit_request(delete, endpoint)

    def get_concurrent_sessions(self):
        """
        Retrieve concurrent sessions
        """
        endpoint = '/'.join([self.endpoint.rpartition('/')[0], 'statistics', 'sessions'])
        return self._submit_request(get, endpoint)
