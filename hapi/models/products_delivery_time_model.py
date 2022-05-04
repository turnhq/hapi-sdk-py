# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ProductsDeliveryTimeModel(object):

    """Implementation of the 'ProductsDeliveryTime' model.

    TODO: type model description here.

    Attributes:
        days_to_process (float): TODO: type description here.
        days_to_setup (float): TODO: type description here.
        total_days (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "days_to_process": 'days_to_process',
        "days_to_setup": 'days_to_setup',
        "total_days": 'total_days'
    }

    def __init__(self,
                 days_to_process=None,
                 days_to_setup=None,
                 total_days=None,
                 additional_properties={}):
        """Constructor for the ProductsDeliveryTimeModel class"""

        # Initialize members of the class
        self.days_to_process = days_to_process
        self.days_to_setup = days_to_setup
        self.total_days = total_days

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

        days_to_process = dictionary.get('days_to_process')
        days_to_setup = dictionary.get('days_to_setup')
        total_days = dictionary.get('total_days')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(days_to_process,
                   days_to_setup,
                   total_days,
                   dictionary)
