# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class OrderedProductsStatusItemModel(object):

    """Implementation of the 'orderedProductsStatusItem' model.

    TODO: type model description here.

    Attributes:
        product_id (string): TODO: type description here.
        status (ChannelStatusEnum): Status of the product. One of the
            following
        status_description (string): Additional information about product
            status

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_id": 'productId',
        "status": 'status',
        "status_description": 'statusDescription'
    }

    def __init__(self,
                 product_id=None,
                 status=None,
                 status_description=None,
                 additional_properties={}):
        """Constructor for the OrderedProductsStatusItemModel class"""

        # Initialize members of the class
        self.product_id = product_id
        self.status = status
        self.status_description = status_description

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
        status = dictionary.get('status')
        status_description = dictionary.get('statusDescription')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(product_id,
                   status,
                   status_description,
                   dictionary)
