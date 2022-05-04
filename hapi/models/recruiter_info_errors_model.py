# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class RecruiterInfoErrorsModel(object):

    """Implementation of the 'RecruiterInfoErrors' model.

    TODO: type model description here.

    Attributes:
        name (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name'
    }

    def __init__(self,
                 name=None,
                 additional_properties={}):
        """Constructor for the RecruiterInfoErrorsModel class"""

        # Initialize members of the class
        self.name = name

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

        name = dictionary.get('name')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   dictionary)
