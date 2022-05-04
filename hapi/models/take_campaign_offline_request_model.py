# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TakeCampaignOfflineRequestModel(object):

    """Implementation of the 'TakeCampaignOfflineRequest' model.

    TODO: type model description here.

    Attributes:
        campaign_id (string): TODO: type description here.
        status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "campaign_id": 'campaignId',
        "status": 'status'
    }

    def __init__(self,
                 campaign_id=None,
                 status=None,
                 additional_properties={}):
        """Constructor for the TakeCampaignOfflineRequestModel class"""

        # Initialize members of the class
        self.campaign_id = campaign_id
        self.status = status

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
        status = dictionary.get('status')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(campaign_id,
                   status,
                   dictionary)
