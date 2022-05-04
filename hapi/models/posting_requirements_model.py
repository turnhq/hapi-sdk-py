# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PostingRequirementsModel(object):

    """Implementation of the 'PostingRequirements' model.

    TODO: type model description here.

    Attributes:
        some_text (string): TODO: type description here.
        multiple_select_field (list of string): TODO: type description here.
        some_int_value (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "some_text": 'someText',
        "multiple_select_field": 'multipleSelectField',
        "some_int_value": 'someIntValue'
    }

    def __init__(self,
                 some_text=None,
                 multiple_select_field=None,
                 some_int_value=None,
                 additional_properties={}):
        """Constructor for the PostingRequirementsModel class"""

        # Initialize members of the class
        self.some_text = some_text
        self.multiple_select_field = multiple_select_field
        self.some_int_value = some_int_value

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

        some_text = dictionary.get('someText')
        multiple_select_field = dictionary.get('multipleSelectField')
        some_int_value = dictionary.get('someIntValue')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(some_text,
                   multiple_select_field,
                   some_int_value,
                   dictionary)
