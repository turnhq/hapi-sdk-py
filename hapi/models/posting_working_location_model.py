# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PostingWorkingLocationModel(object):

    """Implementation of the 'PostingWorkingLocation' model.

    TODO: type model description here.

    Attributes:
        address_line_1 (string): TODO: type description here.
        address_line_2 (string): TODO: type description here.
        postcode (string): TODO: type description here.
        city (string): TODO: type description here.
        country (string): TODO: type description here.
        allows_remote_work (float): Optional parameter allowing remote work,
            possible values are 0 and 1, defaults to 0

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_line_1": 'addressLine1',
        "postcode": 'postcode',
        "city": 'city',
        "country": 'country',
        "address_line_2": 'addressLine2',
        "allows_remote_work": 'allowsRemoteWork'
    }

    def __init__(self,
                 address_line_1=None,
                 postcode=None,
                 city=None,
                 country=None,
                 address_line_2=None,
                 allows_remote_work=None,
                 additional_properties={}):
        """Constructor for the PostingWorkingLocationModel class"""

        # Initialize members of the class
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.postcode = postcode
        self.city = city
        self.country = country
        self.allows_remote_work = allows_remote_work

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

        address_line_1 = dictionary.get('addressLine1')
        postcode = dictionary.get('postcode')
        city = dictionary.get('city')
        country = dictionary.get('country')
        address_line_2 = dictionary.get('addressLine2')
        allows_remote_work = dictionary.get('allowsRemoteWork')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(address_line_1,
                   postcode,
                   city,
                   country,
                   address_line_2,
                   allows_remote_work,
                   dictionary)
