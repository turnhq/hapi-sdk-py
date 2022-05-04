# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PostingOrganizationModel(object):

    """Implementation of the 'PostingOrganization' model.

    TODO: type model description here.

    Attributes:
        name (string): Name of the Company
        company_logo (string): The company Logo that wants to be used on the
            posting. It has to be publicly available so it's picked up and
            used for the different publishing platforms

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "company_logo": 'companyLogo'
    }

    def __init__(self,
                 name=None,
                 company_logo=None,
                 additional_properties={}):
        """Constructor for the PostingOrganizationModel class"""

        # Initialize members of the class
        self.name = name
        self.company_logo = company_logo

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
        company_logo = dictionary.get('companyLogo')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   company_logo,
                   dictionary)
