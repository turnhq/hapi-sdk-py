# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Token:

    def __init__(self, x_auth_token):
        self._x_auth_token = x_auth_token

    def validate_arguments(self):
        if self._x_auth_token:
            return True
        return False

    def apply(self, http_request):
        """ Add custom authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication will be added.

        """
        http_request.add_header("X-Auth-Token", self._x_auth_token)

    def error_message(self):
        """Display error message on occurrence of authentication faliure
        in Token

        """
        return "Token: _x_auth_token is undefined."
