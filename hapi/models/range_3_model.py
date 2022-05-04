# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Range3Model(object):

    """Implementation of the 'range3' model.

    TODO: type model description here.

    Attributes:
        mfrom (float): Minimum salary indication of the indicated period, if
            given, cannot be greater  than 'to', but equal to 'to' is allowed.
            This integer value should be specified in units (not cents).
        to (float): Maximum salary indication of the indicated period. This
            integer value should be specified in units (not cents).
        currency (string): The currency in which the range amount is
            expressed. Must be a valid ISO-4217 value.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "to": 'to',
        "mfrom": 'from',
        "currency": 'currency'
    }

    def __init__(self,
                 to=None,
                 mfrom=None,
                 currency=None,
                 additional_properties={}):
        """Constructor for the Range3Model class"""

        # Initialize members of the class
        self.mfrom = mfrom
        self.to = to
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

        to = dictionary.get('to')
        mfrom = dictionary.get('from')
        currency = dictionary.get('currency')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(to,
                   mfrom,
                   currency,
                   dictionary)
