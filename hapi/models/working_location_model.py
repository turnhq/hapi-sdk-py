# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class WorkingLocationModel(object):

    """Implementation of the 'WorkingLocation' model.

    TODO: type model description here.

    Attributes:
        address_line_1 (list of string): TODO: type description here.
        postcode (list of string): TODO: type description here.
        city (list of string): TODO: type description here.
        country (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_line_1": 'addressLine1',
        "postcode": 'postcode',
        "city": 'city',
        "country": 'country'
    }

    def __init__(self,
                 address_line_1=None,
                 postcode=None,
                 city=None,
                 country=None,
                 additional_properties={}):
        """Constructor for the WorkingLocationModel class"""

        # Initialize members of the class
        self.address_line_1 = address_line_1
        self.postcode = postcode
        self.city = city
        self.country = country

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
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(address_line_1,
                   postcode,
                   city,
                   country,
                   dictionary)
