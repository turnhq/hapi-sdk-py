# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.api_helper import APIHelper
from hapi.models.product_lite_model import ProductLiteModel
from hapi.models.purchase_price_model import PurchasePriceModel


class CreateContractResponseModel(object):

    """Implementation of the 'CreateContractResponse' model.

    TODO: type model description here.

    Attributes:
        customer_id (string): TODO: type description here.
        contract_id (string): TODO: type description here.
        channel_id (int): TODO: type description here.
        credentials (string): TODO: type description here.
        class_name (string): TODO: type description here.
        facets (object): TODO: type description here.
        product (ProductLiteModel): TODO: type description here.
        posting_requirements (string): TODO: type description here.
        expiry_date (datetime): TODO: type description here.
        credits (int): TODO: type description here.
        purchase_price (PurchasePriceModel): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_id": 'customer_id',
        "contract_id": 'contract_id',
        "channel_id": 'channel_id',
        "credentials": 'credentials',
        "class_name": 'class_name',
        "facets": 'facets',
        "product": 'product',
        "posting_requirements": 'posting_requirements',
        "expiry_date": 'expiry_date',
        "credits": 'credits',
        "purchase_price": 'purchase_price'
    }

    def __init__(self,
                 customer_id=None,
                 contract_id=None,
                 channel_id=None,
                 credentials=None,
                 class_name=None,
                 facets=None,
                 product=None,
                 posting_requirements=None,
                 expiry_date=None,
                 credits=None,
                 purchase_price=None,
                 additional_properties={}):
        """Constructor for the CreateContractResponseModel class"""

        # Initialize members of the class
        self.customer_id = customer_id
        self.contract_id = contract_id
        self.channel_id = channel_id
        self.credentials = credentials
        self.class_name = class_name
        self.facets = facets
        self.product = product
        self.posting_requirements = posting_requirements
        self.expiry_date = APIHelper.RFC3339DateTime(expiry_date) if expiry_date else None
        self.credits = credits
        self.purchase_price = purchase_price

        # Add additional model properties to the instance
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        customer_id = dictionary.get('customer_id')
        contract_id = dictionary.get('contract_id')
        channel_id = dictionary.get('channel_id')
        credentials = dictionary.get('credentials')
        class_name = dictionary.get('class_name')
        facets = dictionary.get('facets')
        product = ProductLiteModel.from_dictionary(dictionary.get('product')) if dictionary.get('product') else None
        posting_requirements = dictionary.get('posting_requirements')
        expiry_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("expiry_date")).datetime if dictionary.get("expiry_date") else None
        credits = dictionary.get('credits')
        purchase_price = PurchasePriceModel.from_dictionary(dictionary.get('purchase_price')) if dictionary.get('purchase_price') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(customer_id,
                   contract_id,
                   channel_id,
                   credentials,
                   class_name,
                   facets,
                   product,
                   posting_requirements,
                   expiry_date,
                   credits,
                   purchase_price,
                   dictionary)
