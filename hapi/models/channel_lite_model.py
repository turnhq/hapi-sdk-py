# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ChannelLiteModel(object):

    """Implementation of the 'ChannelLite' model.

    TODO: type model description here.

    Attributes:
        mc_enabled (bool): TODO: type description here.
        id (int): TODO: type description here.
        name (string): TODO: type description here.
        url (string): TODO: type description here.
        mtype (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mc_enabled": 'mc_enabled',
        "id": 'id',
        "name": 'name',
        "url": 'url',
        "mtype": 'type'
    }

    def __init__(self,
                 mc_enabled=None,
                 id=None,
                 name=None,
                 url=None,
                 mtype=None,
                 additional_properties={}):
        """Constructor for the ChannelLiteModel class"""

        # Initialize members of the class
        self.mc_enabled = mc_enabled
        self.id = id
        self.name = name
        self.url = url
        self.mtype = mtype

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

        mc_enabled = dictionary.get('mc_enabled')
        id = dictionary.get('id')
        name = dictionary.get('name')
        url = dictionary.get('url')
        mtype = dictionary.get('type')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(mc_enabled,
                   id,
                   name,
                   url,
                   mtype,
                   dictionary)
