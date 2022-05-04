# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PurchasePriceModel(object):

    """Implementation of the 'PurchasePrice' model.

    TODO: type model description here.

    Attributes:
        currency (string): TODO: type description here.
        amount (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency": 'currency',
        "amount": 'amount'
    }

    def __init__(self,
                 currency=None,
                 amount=None,
                 additional_properties={}):
        """Constructor for the PurchasePriceModel class"""

        # Initialize members of the class
        self.currency = currency
        self.amount = amount

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

        currency = dictionary.get('currency')
        amount = dictionary.get('amount')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(currency,
                   amount,
                   dictionary)
