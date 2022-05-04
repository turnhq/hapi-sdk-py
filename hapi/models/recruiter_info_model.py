# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class RecruiterInfoModel(object):

    """Implementation of the 'recruiterInfo' model.

    Recruiter is the user creating the campaign and you may want to use this
    to provide filtering by recruiter for groups sharing an account.

    Attributes:
        id (string): A vendor-related unique identification for the Recruiter
        name (string): TODO: type description here.
        email_address (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "id": 'id',
        "email_address": 'emailAddress'
    }

    def __init__(self,
                 name=None,
                 id=None,
                 email_address=None,
                 additional_properties={}):
        """Constructor for the RecruiterInfoModel class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.email_address = email_address

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
        email_address = dictionary.get('emailAddress')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   id,
                   email_address,
                   dictionary)
