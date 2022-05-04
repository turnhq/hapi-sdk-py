# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AutocompleteValuesResponseModel(object):

    """Implementation of the 'AutocompleteValuesResponse' model.

    TODO: type model description here.

    Attributes:
        key (string): TODO: type description here.
        label (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": 'key',
        "label": 'label'
    }

    def __init__(self,
                 key=None,
                 label=None,
                 additional_properties={}):
        """Constructor for the AutocompleteValuesResponseModel class"""

        # Initialize members of the class
        self.key = key
        self.label = label

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

        key = dictionary.get('key')
        label = dictionary.get('label')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(key,
                   label,
                   dictionary)
