# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.posting_requirements_model import PostingRequirementsModel


class OrderedProductsPostElementModel(object):

    """Implementation of the 'OrderedProductsPostElement' model.

    TODO: type model description here.

    Attributes:
        product_id (string): Product Identification
        utm (string): Query string for UTM parameters  **Pattern:**
            `/^([%.-_!*a-zA-Z0-9]{1,}=[%.-_!*+,;$()a-zA-Z0-9]{1,}[&]{0,}){1,}$/
            `
        contract_id (string): Contract Identifier needed for My Contracts
            product
        posting_requirements (PostingRequirementsModel): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_id": 'productId',
        "utm": 'utm',
        "contract_id": 'contractId',
        "posting_requirements": 'postingRequirements'
    }

    def __init__(self,
                 product_id=None,
                 utm=None,
                 contract_id=None,
                 posting_requirements=None,
                 additional_properties={}):
        """Constructor for the OrderedProductsPostElementModel class"""

        # Initialize members of the class
        self.product_id = product_id
        self.utm = utm
        self.contract_id = contract_id
        self.posting_requirements = posting_requirements

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

        product_id = dictionary.get('productId')
        utm = dictionary.get('utm')
        contract_id = dictionary.get('contractId')
        posting_requirements = PostingRequirementsModel.from_dictionary(dictionary.get('postingRequirements')) if dictionary.get('postingRequirements') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(product_id,
                   utm,
                   contract_id,
                   posting_requirements,
                   dictionary)
