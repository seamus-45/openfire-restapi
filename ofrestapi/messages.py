# -*- coding: utf-8 -*-
from requests import (get, post)
from base import Base


class Messages(Base):

    def __init__(self, host, secret, endpoint='/plugins/restapi/v1/messages/users'):
        """
        :param host: Scheme://Host/ for API requests
        :param secret: Shared secret key for API requests
        :param endpoint: Endpoint for API requests
        """
        super(Messages, self).__init__(host, secret, endpoint)

    def send_broadcast(self, message):
        """
        Send a broadcast/server message to all online users

        :param message: Message to be send
        """
        payload = {
            'body': message,
        }
        return self._submit_request(post, self.endpoint, json=payload)

    def get_unread_messages(self, jid):
        """
        Retrieve unread messages count

        :param jid: The JID for get messages count from
        """
        endpoint = '/plugins/restapi/v1/archive/messages/unread/' + jid
        return self._submit_request(get, endpoint)
