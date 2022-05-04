# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class FacetOptionShowFacetsModel(object):

    """Implementation of the 'FacetOptionShowFacets' model.

    TODO: type model description here.

    Attributes:
        facet (string): The facet name that becomes required when this option
            is chosen.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "facet": 'facet'
    }

    def __init__(self,
                 facet=None,
                 additional_properties={}):
        """Constructor for the FacetOptionShowFacetsModel class"""

        # Initialize members of the class
        self.facet = facet

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

        facet = dictionary.get('facet')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(facet,
                   dictionary)
