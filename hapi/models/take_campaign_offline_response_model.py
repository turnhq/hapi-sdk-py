# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TakeCampaignOfflineResponseModel(object):

    """Implementation of the 'TakeCampaignOfflineResponse' model.

    TODO: type model description here.

    Attributes:
        campaign_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "campaign_id": 'campaignId'
    }

    def __init__(self,
                 campaign_id=None,
                 additional_properties={}):
        """Constructor for the TakeCampaignOfflineResponseModel class"""

        # Initialize members of the class
        self.campaign_id = campaign_id

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

        campaign_id = dictionary.get('campaignId')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(campaign_id,
                   dictionary)
