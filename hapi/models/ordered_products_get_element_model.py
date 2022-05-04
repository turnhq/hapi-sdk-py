# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.duration_model import DurationModel
from hapi.models.posting_requirements_model import PostingRequirementsModel


class OrderedProductsGetElementModel(object):

    """Implementation of the 'OrderedProductsGetElement' model.

    TODO: type model description here.

    Attributes:
        product_id (string): Product Identification
        status (string): Status per product
        status_description (string): Status description, additional status
            information
        delivered_on (string): Date when the channel went online
        duration (string): How long will the `Product` be online. [DEPRECATED]
            please instead use the `durationPeriod`
        duration_period (DurationModel): TODO: type description here.
        utm (string): Tracking codes
        job_board_link (string): Link to the job ad on the channel. Sometimes
            this link is not available from a job board, then the product
            homepage is returned.
        contract_id (string): Contract Identifier for My Contracts product
        posting_requirements (PostingRequirementsModel): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_id": 'productId',
        "status": 'status',
        "status_description": 'statusDescription',
        "delivered_on": 'deliveredOn',
        "duration": 'duration',
        "duration_period": 'durationPeriod',
        "utm": 'utm',
        "job_board_link": 'jobBoardLink',
        "contract_id": 'contractId',
        "posting_requirements": 'postingRequirements'
    }

    def __init__(self,
                 product_id=None,
                 status=None,
                 status_description=None,
                 delivered_on=None,
                 duration=None,
                 duration_period=None,
                 utm=None,
                 job_board_link=None,
                 contract_id=None,
                 posting_requirements=None,
                 additional_properties={}):
        """Constructor for the OrderedProductsGetElementModel class"""

        # Initialize members of the class
        self.product_id = product_id
        self.status = status
        self.status_description = status_description
        self.delivered_on = delivered_on
        self.duration = duration
        self.duration_period = duration_period
        self.utm = utm
        self.job_board_link = job_board_link
        self.contract_id = contract_id
        self.posting_requirements = posting_requirements

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

        product_id = dictionary.get('productId')
        status = dictionary.get('status')
        status_description = dictionary.get('statusDescription')
        delivered_on = dictionary.get('deliveredOn')
        duration = dictionary.get('duration')
        duration_period = DurationModel.from_dictionary(dictionary.get('durationPeriod')) if dictionary.get('durationPeriod') else None
        utm = dictionary.get('utm')
        job_board_link = dictionary.get('jobBoardLink')
        contract_id = dictionary.get('contractId')
        posting_requirements = PostingRequirementsModel.from_dictionary(dictionary.get('postingRequirements')) if dictionary.get('postingRequirements') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(product_id,
                   status,
                   status_description,
                   delivered_on,
                   duration,
                   duration_period,
                   utm,
                   job_board_link,
                   contract_id,
                   posting_requirements,
                   dictionary)
