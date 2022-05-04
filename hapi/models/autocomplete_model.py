# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AutocompleteModel(object):

    """Implementation of the 'Autocomplete' model.

    Used for Facets whose value choices need to be fetched through an
    additional call to the [List autocomplete values for posting
    requirements](https://vonq.stoplight.io/docs/hapi/b3A6MzM2MDEzODk-list-auto
    complete-values-for-posting-requirement) endpoint.

    Attributes:
        required_parameters (list of RequiredParameterEnum): List of keys to
            pass to  the body of the request calling the [List autocomplete
            values for posting
            requirements](https://vonq.stoplight.io/docs/hapi/b3A6MzM2MDEzODk-l
            ist-autocomplete-values-for-posting-requirement) endpoint.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "required_parameters": 'required_parameters'
    }

    def __init__(self,
                 required_parameters=None,
                 additional_properties={}):
        """Constructor for the AutocompleteModel class"""

        # Initialize members of the class
        self.required_parameters = required_parameters

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

        required_parameters = dictionary.get('required_parameters')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(required_parameters,
                   dictionary)
