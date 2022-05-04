# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.ordered_products_post_element_model import OrderedProductsPostElementModel
from hapi.models.posting_details_model import PostingDetailsModel
from hapi.models.recruiter_info_model import RecruiterInfoModel
from hapi.models.target_group_model import TargetGroupModel


class CampaignOrderModel(object):

    """Implementation of the 'CampaignOrder' model.

    TODO: type model description here.

    Attributes:
        company_id (string): A vendor-related unique identification for the
            Company that's making the order. Doesn't affect the order process
            at all, but provides a method for later filtering by this
            identification. It's also used when creating a unified report of
            Campaign orders made in a period of time.
        order_reference (string): A vendor-related Reference number for the
            order. This could be a PO number or an Invoice number. Doesn't
            affect the order process at all, but provides a way for the ATS to
            identify the specific order for their internal billing process
            Maximum length of this field is 80 symbols
        currency (string): An ISO 4217 code for a currency to use for order
            invoicing. Currently only GBP and USD are supported. Default
            currency is EUR.
        recruiter_info (RecruiterInfoModel): Recruiter is the user creating
            the campaign and you may want to use this to provide filtering by
            recruiter for groups sharing an account.
        campaign_name (string): Campaign name as it's going to be listed.
            Doesn't have to resemble the Posting Title. For example, the
            Campaign name could be **Software Development Manager** while the
            Posting title could be **Want to lead a Team of Software
            Developers? Join us**
        posting_details (PostingDetailsModel): TODO: type description here.
        target_group (TargetGroupModel): TODO: type description here.
        ordered_products (list of string): A list of the Products selected by
            the user.
        ordered_products_specs (list of OrderedProductsPostElementModel):
            Specification object for some of the ordered products

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "company_id": 'companyId',
        "recruiter_info": 'recruiterInfo',
        "posting_details": 'postingDetails',
        "target_group": 'targetGroup',
        "ordered_products": 'orderedProducts',
        "order_reference": 'orderReference',
        "currency": 'currency',
        "campaign_name": 'campaignName',
        "ordered_products_specs": 'orderedProductsSpecs'
    }

    def __init__(self,
                 company_id=None,
                 recruiter_info=None,
                 posting_details=None,
                 target_group=None,
                 ordered_products=None,
                 order_reference=None,
                 currency=None,
                 campaign_name=None,
                 ordered_products_specs=None,
                 additional_properties={}):
        """Constructor for the CampaignOrderModel class"""

        # Initialize members of the class
        self.company_id = company_id
        self.order_reference = order_reference
        self.currency = currency
        self.recruiter_info = recruiter_info
        self.campaign_name = campaign_name
        self.posting_details = posting_details
        self.target_group = target_group
        self.ordered_products = ordered_products
        self.ordered_products_specs = ordered_products_specs

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

        company_id = dictionary.get('companyId')
        recruiter_info = RecruiterInfoModel.from_dictionary(dictionary.get('recruiterInfo')) if dictionary.get('recruiterInfo') else None
        posting_details = PostingDetailsModel.from_dictionary(dictionary.get('postingDetails')) if dictionary.get('postingDetails') else None
        target_group = TargetGroupModel.from_dictionary(dictionary.get('targetGroup')) if dictionary.get('targetGroup') else None
        ordered_products = dictionary.get('orderedProducts')
        order_reference = dictionary.get('orderReference')
        currency = dictionary.get('currency')
        campaign_name = dictionary.get('campaignName')
        ordered_products_specs = None
        if dictionary.get('orderedProductsSpecs') is not None:
            ordered_products_specs = [OrderedProductsPostElementModel.from_dictionary(x) for x in dictionary.get('orderedProductsSpecs')]
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(company_id,
                   recruiter_info,
                   posting_details,
                   target_group,
                   ordered_products,
                   order_reference,
                   currency,
                   campaign_name,
                   ordered_products_specs,
                   dictionary)
