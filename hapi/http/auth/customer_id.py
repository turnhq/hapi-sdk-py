# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CustomerId:

    def __init__(self, x_customer_id):
        self._x_customer_id = x_customer_id

    def validate_arguments(self):
        if self._x_customer_id:
            return True
        return False

    def apply(self, http_request):
        """ Add custom authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication will be added.

        """
        http_request.add_header("X-Customer-Id", self._x_customer_id)

    def error_message(self):
        """Display error message on occurrence of authentication faliure
        in CustomerId

        """
        return "CustomerId: _x_customer_id is undefined."
