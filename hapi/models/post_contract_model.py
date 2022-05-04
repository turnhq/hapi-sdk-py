# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.api_helper import APIHelper
from hapi.models.contract_purchase_price_model import ContractPurchasePriceModel


class PostContractModel(object):

    """Implementation of the 'PostContract' model.

    TODO: type model description here.

    Attributes:
        channel_id (float): TODO: type description here.
        credentials (object): An object with credentials data
        facets (object): An object with product parameters
        followed_instructions (bool): When creating contracts for Channels
            that require the end-user to follow instructions (based on the
            `manual_setup_required` key in the response body for the [Retrieve
            details for channel with support for
            contracts](https://vonq.stoplight.io/docs/hapi/b3A6NTUxMjYwODI-retr
            ieve-details-for-channel-with-support-for-contracts) endpoint),
            set this value to `true` to confirm the user has done so. For
            quality purposes, setting this field to `true` for Channels that
            don't require following instructions will result in a 400 Bad
            Request.
        expiry_date (datetime): TODO: type description here.
        credits (float): TODO: type description here.
        purchase_price (ContractPurchasePriceModel): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "channel_id": 'channel_id',
        "credentials": 'credentials',
        "facets": 'facets',
        "followed_instructions": 'followed_instructions',
        "expiry_date": 'expiry_date',
        "credits": 'credits',
        "purchase_price": 'purchase_price'
    }

    def __init__(self,
                 channel_id=None,
                 credentials=None,
                 facets=None,
                 followed_instructions=None,
                 expiry_date=None,
                 credits=None,
                 purchase_price=None,
                 additional_properties={}):
        """Constructor for the PostContractModel class"""

        # Initialize members of the class
        self.channel_id = channel_id
        self.credentials = credentials
        self.facets = facets
        self.followed_instructions = followed_instructions
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

        channel_id = dictionary.get('channel_id')
        credentials = dictionary.get('credentials')
        facets = dictionary.get('facets')
        followed_instructions = dictionary.get('followed_instructions')
        expiry_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("expiry_date")).datetime if dictionary.get("expiry_date") else None
        credits = dictionary.get('credits')
        purchase_price = ContractPurchasePriceModel.from_dictionary(dictionary.get('purchase_price')) if dictionary.get('purchase_price') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(channel_id,
                   credentials,
                   facets,
                   followed_instructions,
                   expiry_date,
                   credits,
                   purchase_price,
                   dictionary)
