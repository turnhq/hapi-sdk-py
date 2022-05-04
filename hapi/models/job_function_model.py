# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class JobFunctionModel(object):

    """Implementation of the 'JobFunction' model.

    JobFunction(id, name, parent)

    Attributes:
        id (float): TODO: type description here.
        name (string): TODO: type description here.
        parent (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "id": 'id',
        "parent": 'parent'
    }

    def __init__(self,
                 name=None,
                 id=None,
                 parent=None,
                 additional_properties={}):
        """Constructor for the JobFunctionModel class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.parent = parent

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
        id = dictionary.get('id')
        parent = dictionary.get('parent')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   id,
                   parent,
                   dictionary)
