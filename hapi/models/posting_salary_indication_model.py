# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.range_3_model import Range3Model


class PostingSalaryIndicationModel(object):

    """Implementation of the 'PostingSalaryIndication' model.

    TODO: type model description here.

    Attributes:
        period (PeriodEnum): TODO: type description here.
        range (Range3Model): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "period": 'period',
        "range": 'range'
    }

    def __init__(self,
                 period=None,
                 range=None,
                 additional_properties={}):
        """Constructor for the PostingSalaryIndicationModel class"""

        # Initialize members of the class
        self.period = period
        self.range = range

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

        period = dictionary.get('period')
        range = Range3Model.from_dictionary(dictionary.get('range')) if dictionary.get('range') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(period,
                   range,
                   dictionary)
