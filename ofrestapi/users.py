# -*- coding: utf-8 -*-
from requests import (get, put, post, delete)
from base import Base


class Users(Base):
    SUBSCRIPTION_REMOVE = -1
    SUBSCRIPTION_NONE = 0
    SUBSCRIPTION_TO = 1
    SUBSCRIPTION_FROM = 2
    SUBSCRIPTION_BOTH = 3

    def __init__(self, host, secret, endpoint='/plugins/restapi/v1/users'):
        """
        :param host: Scheme://Host/ for API requests
        :param secret: Shared secret key for API request
        :param endpoint: Endpoint for API request
        """
        super(Users, self).__init__(host, secret, endpoint)

    def get_user(self, username):
        """
        Retrieve exact user info

        :param username: The exact user name for request
        """
        endpoint = '/'.join([self.endpoint, username])
        return self._submit_request(get, endpoint)

    def get_users(self, query=None):
        """
        Retrieve all users or filter by user name

        :param query: (optional) Search/Filter by user name. This act like the wildcard search %String%
        """
        params = {'search': query} if query else None
        return self._submit_request(get, self.endpoint, params=params)

    def add_user(self, username, password, name=None, email=None, props=None):
        """
        Add user

        :param username: The user name
        :param password: The password of the user
        :param name: (optional) The display name of the user
        :param email: (optional) The email address of the user
        :param props: (optional) Dictionary with additional user properties
        """
        payload = {
            'username': username,
            'password': password,
            'name': name,
            'email': email,
        }
        if props:
            payload['properties'] = {}
            payload['properties']['property'] = []
            for key, value in props.iteritems():
                payload['properties']['property'].append({'@key': key, '@value': value})
        return self._submit_request(post, self.endpoint, json=payload)

    def delete_user(self, username):
        """
        Delete user

        :param username: The user name
        """
        endpoint = '/'.join([self.endpoint, username])
        return self._submit_request(delete, endpoint)

    def update_user(self, username, newusername=None, password=None, name=None, email=None, props=None):
        """
        Update user.

        :param username: The user name
        :param newusername: (optional) The new user name of the user
        :param password: (optional) The new password of the user
        :param name: (optional) The new display name of the user
        :param email: (optional) The new email address of the use
        :param props: (optional) Dictionary with additional user properties
        """
        endpoint = '/'.join([self.endpoint, username])
        payload = {
            'username': newusername if newusername else username,
            'password': password,
            'name': name,
            'email': email,
        }
        if props:
            payload['properties'] = {}
            payload['properties']['property'] = []
            for key, value in props.iteritems():
                payload['properties']['property'].append({'@key': key, '@value': value})
        return self._submit_request(put, endpoint, json=payload)

    def get_user_groups(self, username):
        """
        Retrieve all user groups

        :param username: The user name
        """
        endpoint = '/'.join([self.endpoint, username, 'groups'])
        return self._submit_request(get, endpoint)

    def add_user_groups(self, username, groups):
        """
        Add user to one or more groups

        :param username: The user name
        :param groups: One or more groups to be added in
        :type groups: List of strings. E.g. ['Admins','Friends']
        """
        endpoint = '/'.join([self.endpoint, username, 'groups'])
        payload = {
            'groupname': groups,
        }
        return self._submit_request(post, endpoint, json=payload)

    def delete_user_groups(self, username, groups):
        """
        Remove user from one or more groups

        :param username: The user name
        :param groups: One or more groups to be removed from
        :type groups: List of strings. E.g. ['Admins','Friends']
        """
        endpoint = '/'.join([self.endpoint, username, 'groups'])
        payload = {
            'groupname': groups,
        }
        return self._submit_request(delete, endpoint, json=payload)

    def lock_user(self, username):
        """
        Lockout a user

        :param username: The user name
        """
        endpoint = '/'.join([self.endpoint.rpartition('/')[0], 'lockouts', username])
        return self._submit_request(post, endpoint)

    def unlock_user(self, username):
        """
        Unlock a user

        :param username: The user name
        """
        endpoint = '/'.join([self.endpoint.rpartition('/')[0], 'lockouts', username])
        return self._submit_request(delete, endpoint)

    def get_user_roster(self, username):
        """
        Retrieve user roster

        :param username: The user name
        """
        endpoint = '/'.join([self.endpoint, username, 'roster'])
        return self._submit_request(get, endpoint)

    def add_user_roster_item(self, username, jid, name=None, subscription=None, groups=None):
        """
        Add a user roster entry

        :param username: The user name
        :param jid: The JID of the roster item to be added. E.g. foo@example.org
        :param name: (optional) The nickname for the user when used in this roster
        :param subscription: (optional) The subscription type. One of SUBSCRIPTION_REMOVE, SUBSCRIPTION_NONE,SUBSCRIPTION_TO,SUBSCRIPTION_FROM,SUBSCRIPTION_BOTH
        :param groups: (optional) A list of groups to organize roster entries under
        :type groups: List of strings. E.g. ['Admins','Friends']
        """
        endpoint = '/'.join([self.endpoint, username, 'roster'])
        payload = {
            'jid': jid,
            'nickname': name,
            'subscriptionType': subscription,
            'groups': {'group': groups},
        }
        return self._submit_request(post, endpoint, json=payload)

    def delete_user_roster_item(self, username, jid):
        """
        Delete a user roster entry

        :param username: The user name
        :param jid: The JID of the roster item to be deleted. E.g. foo@example.org
        """
        endpoint = '/'.join([self.endpoint, username, 'roster', jid])
        return self._submit_request(delete, endpoint)

    def update_user_roster_item(self, username, jid, name=None, subscription=None, groups=None):
        """
        Update a user roster entry

        :param username: The user name
        :param jid: The JID of the roster item to be updated. E.g. foo@example.org
        :param name: (optional) The nickname for the user when used in this roster
        :param subscription: (optional) The subscription type. One of SUBSCRIPTION_REMOVE, SUBSCRIPTION_NONE,SUBSCRIPTION_TO,SUBSCRIPTION_FROM,SUBSCRIPTION_BOTH
        :param groups: (optional) A list of groups to organize roster entries under
        :type groups: List of strings. E.g. ['Admins','Friends']
        """
        endpoint = '/'.join([self.endpoint, username, 'roster', jid])
        payload = {
            'jid': jid,
            'nickname': name,
            'subscriptionType': subscription,
            'groups': {'group': groups},
        }
        return self._submit_request(put, endpoint, json=payload)
