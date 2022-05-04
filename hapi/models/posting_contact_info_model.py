# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PostingContactInfoModel(object):

    """Implementation of the 'PostingContactInfo' model.

    Contact is whom to contact about the job. This may be part of the posting
    info for candidates to know whom they can reach out to learn more about
    the vacancy.

    Attributes:
        name (string): TODO: type description here.
        phone_number (string): TODO: type description here.
        email_address (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "phone_number": 'phoneNumber',
        "email_address": 'emailAddress'
    }

    def __init__(self,
                 name=None,
                 phone_number=None,
                 email_address=None,
                 additional_properties={}):
        """Constructor for the PostingContactInfoModel class"""

        # Initialize members of the class
        self.name = name
        self.phone_number = phone_number
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
        phone_number = dictionary.get('phoneNumber')
        email_address = dictionary.get('emailAddress')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   phone_number,
                   email_address,
                   dictionary)
