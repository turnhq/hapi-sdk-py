# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.name_model import NameModel


class EducationLevelModel(object):

    """Implementation of the 'EducationLevel' model.

    TODO: type model description here.

    Attributes:
        id (int): Internal Identification for an Education Level
        name (list of NameModel): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 additional_properties={}):
        """Constructor for the EducationLevelModel class"""

        # Initialize members of the class
        self.id = id
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

        id = dictionary.get('id')
        name = None
        if dictionary.get('name') is not None:
            name = [NameModel.from_dictionary(x) for x in dictionary.get('name')]
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   name,
                   dictionary)
