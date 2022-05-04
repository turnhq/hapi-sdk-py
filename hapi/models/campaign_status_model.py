# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.ordered_products_status_item_model import OrderedProductsStatusItemModel


class CampaignStatusModel(object):

    """Implementation of the 'CampaignStatus' model.

    TODO: type model description here.

    Attributes:
        campaign_id (string): TODO: type description here.
        status (StatusEnum): Status of the campaign. One of the following
        ordered_products_statuses (list of OrderedProductsStatusItemModel):
            TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "campaign_id": 'campaignId',
        "status": 'status',
        "ordered_products_statuses": 'orderedProductsStatuses'
    }

    def __init__(self,
                 campaign_id=None,
                 status=None,
                 ordered_products_statuses=None,
                 additional_properties={}):
        """Constructor for the CampaignStatusModel class"""

        # Initialize members of the class
        self.campaign_id = campaign_id
        self.status = status
        self.ordered_products_statuses = ordered_products_statuses

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
        ordered_products_statuses = None
        if dictionary.get('orderedProductsStatuses') is not None:
            ordered_products_statuses = [OrderedProductsStatusItemModel.from_dictionary(x) for x in dictionary.get('orderedProductsStatuses')]
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(campaign_id,
                   status,
                   ordered_products_statuses,
                   dictionary)
