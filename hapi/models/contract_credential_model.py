# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ContractCredentialModel(object):

    """Implementation of the 'ContractCredential' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        label (string): TODO: type description here.
        sort (string): TODO: type description here.
        description (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "label": 'label',
        "sort": 'sort',
        "description": 'description'
    }

    def __init__(self,
                 name=None,
                 label=None,
                 sort=None,
                 description=None,
                 additional_properties={}):
        """Constructor for the ContractCredentialModel class"""

        # Initialize members of the class
        self.name = name
        self.label = label
        self.sort = sort
        self.description = description

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
        label = dictionary.get('label')
        sort = dictionary.get('sort')
        description = dictionary.get('description')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   label,
                   sort,
                   description,
                   dictionary)
