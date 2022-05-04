# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.campaign_model import CampaignModel


class ResultSet1Model(object):

    """Implementation of the 'ResultSet1' model.

    TODO: type model description here.

    Attributes:
        total (float): Number of total results
        limit (float): Results page size
        offset (float): Initial starting index for the results
        data (list of CampaignModel): A Page of Campaign Objects

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total": 'total',
        "limit": 'limit',
        "offset": 'offset',
        "data": 'data'
    }

    def __init__(self,
                 total=None,
                 limit=None,
                 offset=None,
                 data=None,
                 additional_properties={}):
        """Constructor for the ResultSet1Model class"""

        # Initialize members of the class
        self.total = total
        self.limit = limit
        self.offset = offset
        self.data = data

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

        total = dictionary.get('total')
        limit = dictionary.get('limit')
        offset = dictionary.get('offset')
        data = None
        if dictionary.get('data') is not None:
            data = [CampaignModel.from_dictionary(x) for x in dictionary.get('data')]
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(total,
                   limit,
                   offset,
                   data,
                   dictionary)
