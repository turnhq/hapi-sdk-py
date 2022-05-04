# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from hapi.api_helper import APIHelper
import hapi.exceptions.api_exception


class TakeCampaignOfflineErrorResponse2Exception(hapi.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the TakeCampaignOfflineErrorResponse2Exception class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(TakeCampaignOfflineErrorResponse2Exception, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.campaign_id = dictionary.get('campaignId')
        self.status = dictionary.get('status')
