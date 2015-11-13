# -*- coding: utf-8 -*-
from requests import post
from base import Base


class Messages(Base):

    def __init__(self, host, secret, endpoint='/plugins/restapi/v1/messages/users'):
        """
        :param host: Scheme://Host/ for API requests
        :param secret: Shared secret key for API request
        :param endpoint: Endpoint for API request
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
