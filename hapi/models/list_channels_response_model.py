# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.channel_lite_model import ChannelLiteModel


class ListChannelsResponseModel(object):

    """Implementation of the 'ListChannelsResponse' model.

    TODO: type model description here.

    Attributes:
        count (int): TODO: type description here.
        next (string): TODO: type description here.
        previous (string): TODO: type description here.
        results (list of ChannelLiteModel): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "results": 'results',
        "next": 'next',
        "previous": 'previous'
    }

    def __init__(self,
                 count=None,
                 results=None,
                 next=None,
                 previous=None,
                 additional_properties={}):
        """Constructor for the ListChannelsResponseModel class"""

        # Initialize members of the class
        self.count = count
        self.next = next
        self.previous = previous
        self.results = results

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

        count = dictionary.get('count')
        results = None
        if dictionary.get('results') is not None:
            results = [ChannelLiteModel.from_dictionary(x) for x in dictionary.get('results')]
        next = dictionary.get('next')
        previous = dictionary.get('previous')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(count,
                   results,
                   next,
                   previous,
                   dictionary)
