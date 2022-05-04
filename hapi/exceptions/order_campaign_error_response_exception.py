# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from hapi.api_helper import APIHelper
import hapi.exceptions.api_exception
from hapi.models.posting_details_errors_model import PostingDetailsErrorsModel
from hapi.models.recruiter_info_errors_model import RecruiterInfoErrorsModel
from hapi.models.ordered_products_spec_model import OrderedProductsSpecModel


class OrderCampaignErrorResponseException(hapi.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the OrderCampaignErrorResponseException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(OrderCampaignErrorResponseException, self).__init__(reason, response)
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
        self.company_id = dictionary.get('companyId')
        self.posting_details = PostingDetailsErrorsModel.from_dictionary(dictionary.get('postingDetails')) if dictionary.get('postingDetails') else None
        self.target_group = dictionary.get('targetGroup')
        self.recruiter_info = RecruiterInfoErrorsModel.from_dictionary(dictionary.get('recruiterInfo')) if dictionary.get('recruiterInfo') else None
        self.ordered_products = dictionary.get('orderedProducts')
        self.ordered_products_specs = None
        if dictionary.get('orderedProductsSpecs') is not None:
            self.ordered_products_specs = [OrderedProductsSpecModel.from_dictionary(x) for x in dictionary.get('orderedProductsSpecs')]
