# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.channel_model import ChannelModel
from hapi.models.industry_model import IndustryModel
from hapi.models.job_function_model import JobFunctionModel
from hapi.models.location_model import LocationModel
from hapi.models.price_model import PriceModel
from hapi.models.time_to_process_model import TimeToProcessModel
from hapi.models.time_to_setup_model import TimeToSetupModel


class ProductModel(object):

    """Implementation of the 'Product' model.

    TODO: type model description here.

    Attributes:
        title (string): TODO: type description here.
        locations (list of LocationModel): TODO: type description here.
        job_functions (list of JobFunctionModel): TODO: type description
            here.
        industries (list of IndustryModel): TODO: type description here.
        description (string): TODO: type description here.
        homepage (string): TODO: type description here.
        logo_url (string): TODO: type description here.
        logo_square_url (string): TODO: type description here.
        logo_rectangle_url (string): TODO: type description here.
        duration (object): TODO: type description here.
        time_to_process (TimeToProcessModel): TODO: type description here.
        time_to_setup (TimeToSetupModel): TODO: type description here.
        product_id (uuid|string): TODO: type description here.
        vonq_price (list of PriceModel): the price to be displayed to
            customers
        ratecard_price (list of PriceModel): TODO: type description here.
        mtype (ChannelTypeEnum): The type of a channel
        cross_postings (list of string): TODO: type description here.
        channel (ChannelModel): TODO: type description here.
        audience_group (AudienceGroupEnum): The product's audience group
            (niche/generic)
        mc_enabled (bool): is My Contract enabled for the channel
        mc_only (bool): is the product available only for My Contract order
        allow_orders (bool): is the product available for order. a campaign
            cannot be ordered with a product having `allow_orders` set to
            `false`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title": 'title',
        "locations": 'locations',
        "job_functions": 'job_functions',
        "industries": 'industries',
        "time_to_process": 'time_to_process',
        "time_to_setup": 'time_to_setup',
        "product_id": 'product_id',
        "vonq_price": 'vonq_price',
        "ratecard_price": 'ratecard_price',
        "mtype": 'type',
        "cross_postings": 'cross_postings',
        "channel": 'channel',
        "audience_group": 'audience_group',
        "mc_enabled": 'mc_enabled',
        "mc_only": 'mc_only',
        "allow_orders": 'allow_orders',
        "description": 'description',
        "homepage": 'homepage',
        "logo_url": 'logo_url',
        "logo_square_url": 'logo_square_url',
        "logo_rectangle_url": 'logo_rectangle_url',
        "duration": 'duration'
    }

    def __init__(self,
                 title=None,
                 locations=None,
                 job_functions=None,
                 industries=None,
                 time_to_process=None,
                 time_to_setup=None,
                 product_id=None,
                 vonq_price=None,
                 ratecard_price=None,
                 mtype=None,
                 cross_postings=None,
                 channel=None,
                 audience_group=None,
                 mc_enabled=None,
                 mc_only=None,
                 allow_orders=None,
                 description=None,
                 homepage=None,
                 logo_url=None,
                 logo_square_url=None,
                 logo_rectangle_url=None,
                 duration=None,
                 additional_properties={}):
        """Constructor for the ProductModel class"""

        # Initialize members of the class
        self.title = title
        self.locations = locations
        self.job_functions = job_functions
        self.industries = industries
        self.description = description
        self.homepage = homepage
        self.logo_url = logo_url
        self.logo_square_url = logo_square_url
        self.logo_rectangle_url = logo_rectangle_url
        self.duration = duration
        self.time_to_process = time_to_process
        self.time_to_setup = time_to_setup
        self.product_id = product_id
        self.vonq_price = vonq_price
        self.ratecard_price = ratecard_price
        self.mtype = mtype
        self.cross_postings = cross_postings
        self.channel = channel
        self.audience_group = audience_group
        self.mc_enabled = mc_enabled
        self.mc_only = mc_only
        self.allow_orders = allow_orders

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

        title = dictionary.get('title')
        locations = None
        if dictionary.get('locations') is not None:
            locations = [LocationModel.from_dictionary(x) for x in dictionary.get('locations')]
        job_functions = None
        if dictionary.get('job_functions') is not None:
            job_functions = [JobFunctionModel.from_dictionary(x) for x in dictionary.get('job_functions')]
        industries = None
        if dictionary.get('industries') is not None:
            industries = [IndustryModel.from_dictionary(x) for x in dictionary.get('industries')]
        time_to_process = TimeToProcessModel.from_dictionary(dictionary.get('time_to_process')) if dictionary.get('time_to_process') else None
        time_to_setup = TimeToSetupModel.from_dictionary(dictionary.get('time_to_setup')) if dictionary.get('time_to_setup') else None
        product_id = dictionary.get('product_id')
        vonq_price = None
        if dictionary.get('vonq_price') is not None:
            vonq_price = [PriceModel.from_dictionary(x) for x in dictionary.get('vonq_price')]
        ratecard_price = None
        if dictionary.get('ratecard_price') is not None:
            ratecard_price = [PriceModel.from_dictionary(x) for x in dictionary.get('ratecard_price')]
        mtype = dictionary.get('type')
        cross_postings = dictionary.get('cross_postings')
        channel = ChannelModel.from_dictionary(dictionary.get('channel')) if dictionary.get('channel') else None
        audience_group = dictionary.get('audience_group')
        mc_enabled = dictionary.get('mc_enabled')
        mc_only = dictionary.get('mc_only')
        allow_orders = dictionary.get('allow_orders')
        description = dictionary.get('description')
        homepage = dictionary.get('homepage')
        logo_url = dictionary.get('logo_url')
        logo_square_url = dictionary.get('logo_square_url')
        logo_rectangle_url = dictionary.get('logo_rectangle_url')
        duration = dictionary.get('duration')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(title,
                   locations,
                   job_functions,
                   industries,
                   time_to_process,
                   time_to_setup,
                   product_id,
                   vonq_price,
                   ratecard_price,
                   mtype,
                   cross_postings,
                   channel,
                   audience_group,
                   mc_enabled,
                   mc_only,
                   allow_orders,
                   description,
                   homepage,
                   logo_url,
                   logo_square_url,
                   logo_rectangle_url,
                   duration,
                   dictionary)
