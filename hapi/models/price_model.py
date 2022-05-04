# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PriceModel(object):

    """Implementation of the 'Price' model.

    TODO: type model description here.

    Attributes:
        amount (float): Price amount in specified currency and 2 decimal
            places
        currency (CurrencyEnum): ISO 4217 code for the Currency.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": 'amount',
        "currency": 'currency'
    }

    def __init__(self,
                 amount=None,
                 currency=None,
                 additional_properties={}):
        """Constructor for the PriceModel class"""

        # Initialize members of the class
        self.amount = amount
        self.currency = currency

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

        amount = dictionary.get('amount')
        currency = dictionary.get('currency')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(amount,
                   currency,
                   dictionary)
