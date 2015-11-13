# -*- coding: utf-8 -*-
from requests import (get, put, post, delete)
from base import Base


class Groups(Base):

    def __init__(self, host, secret, endpoint='/plugins/restapi/v1/groups'):
        """
        :param host: Scheme://Host/ for API requests
        :param secret: Shared secret key for API request
        :param endpoint: Endpoint for API request
        """
        super(Groups, self).__init__(host, secret, endpoint)

    def get_groups(self):
        """
        Retrieve all groups
        """
        return self._submit_request(get, self.endpoint)

    def get_group(self, groupname):
        """
        Retrieve exact group info

        :param groupname: The exact group name for request
        """
        endpoint = '/'.join([self.endpoint, groupname])
        return self._submit_request(get, endpoint)

    def add_group(self, groupname, description):
        """
        Create a group

        :param groupname: Name of the group
        :param description: Description of the group
        """
        payload = {
            'name': groupname,
            'description': description,
        }
        return self._submit_request(post, self.endpoint, json=payload)

    def delete_group(self, groupname):
        """
        Delete a group

        :param groupname: The exact group name for request
        """
        endpoint = '/'.join([self.endpoint, groupname])
        return self._submit_request(delete, endpoint)

    def update_group(self, groupname, description):
        """
        Update a group

        :param groupname: Name of the group
        :param description: Description of the group
        """
        endpoint = '/'.join([self.endpoint, groupname])
        payload = {
            'name': groupname,
            'description': description,
        }
        return self._submit_request(put, endpoint, json=payload)
