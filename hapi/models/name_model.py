# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class NameModel(object):

    """Implementation of the 'name' model.

    TODO: type model description here.

    Attributes:
        language_code (string): ICU Locale code for the Language of the
            Education Level's name
        value (string): Education Level name in one defined Language

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "language_code": 'languageCode',
        "value": 'value'
    }

    def __init__(self,
                 language_code=None,
                 value=None,
                 additional_properties={}):
        """Constructor for the NameModel class"""

        # Initialize members of the class
        self.language_code = language_code
        self.value = value

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

        language_code = dictionary.get('languageCode')
        value = dictionary.get('value')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(language_code,
                   value,
                   dictionary)
