# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.api_helper import APIHelper
from hapi.models.contract_product_model import ContractProductModel
from hapi.models.contract_purchase_price_model import ContractPurchasePriceModel
from hapi.models.facet_model import FacetModel


class ContractModel(object):

    """Implementation of the 'Contract' model.

    TODO: type model description here.

    Attributes:
        contract_id (string): The identifier of the Contract. To be used when
            creating a Campaign
        customer_id (string): The customer_id this contract belongs to. Based
            on the original `X-Customer-Id` header used when the contract was
            created.
        channel_id (float): The Channel (job board) the contract is to be used
            for
        credentials (object): AES Encrypted credentials
        class_name (string): Channel slug
        facets (object): An object with contract parameters
        product (ContractProductModel): The Product to be used in combination
            with the Contract when ordering a Campaign.
        posting_requirements (list of FacetModel): A list of the Contract
            Channel's Facets
        expiry_date (datetime): TODO: type description here.
        credits (float): TODO: type description here.
        purchase_price (ContractPurchasePriceModel): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "contract_id": 'contract_id',
        "customer_id": 'customer_id',
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
                 contract_id=None,
                 customer_id=None,
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
        """Constructor for the ContractModel class"""

        # Initialize members of the class
        self.contract_id = contract_id
        self.customer_id = customer_id
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

        contract_id = dictionary.get('contract_id')
        customer_id = dictionary.get('customer_id')
        channel_id = dictionary.get('channel_id')
        credentials = dictionary.get('credentials')
        class_name = dictionary.get('class_name')
        facets = dictionary.get('facets')
        product = ContractProductModel.from_dictionary(dictionary.get('product')) if dictionary.get('product') else None
        posting_requirements = None
        if dictionary.get('posting_requirements') is not None:
            posting_requirements = [FacetModel.from_dictionary(x) for x in dictionary.get('posting_requirements')]
        expiry_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("expiry_date")).datetime if dictionary.get("expiry_date") else None
        credits = dictionary.get('credits')
        purchase_price = ContractPurchasePriceModel.from_dictionary(dictionary.get('purchase_price')) if dictionary.get('purchase_price') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(contract_id,
                   customer_id,
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
