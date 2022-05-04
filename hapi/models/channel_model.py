# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.contract_credential_model import ContractCredentialModel
from hapi.models.facet_model import FacetModel


class ChannelModel(object):

    """Implementation of the 'Channel' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of a channel
        url (string): The url of a channel
        mtype (ChannelTypeEnum): The type of a channel
        mc_enabled (bool): Does a channel support My Contracts
        contract_credentials (list of ContractCredentialModel): TODO: type
            description here.
        contract_facets (list of object): TODO: type description here.
        posting_requirements (list of FacetModel): Dynamic posting
            requirements for MC products, used to provide additional data with
            vacancies
        manual_setup_required (bool): Some Channels require manual setup done
            by the end-user. In most such cases, `setup_instructions` should
            contain HTML
        setup_instructions (string): Additional setup instructions required to
            post on the Channel
        feed_url (string): Some channels like apec.fr require the user to send
            the job board an XML url. If not null, this value should be
            displayed to the user, along with the `setup_instructions`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "url": 'url',
        "mtype": 'type',
        "mc_enabled": 'mc_enabled',
        "contract_credentials": 'contract_credentials',
        "contract_facets": 'contract_facets',
        "posting_requirements": 'posting_requirements',
        "manual_setup_required": 'manual_setup_required',
        "setup_instructions": 'setup_instructions',
        "feed_url": 'feed_url'
    }

    def __init__(self,
                 name=None,
                 url=None,
                 mtype=None,
                 mc_enabled=None,
                 contract_credentials=None,
                 contract_facets=None,
                 posting_requirements=None,
                 manual_setup_required=None,
                 setup_instructions=None,
                 feed_url=None,
                 additional_properties={}):
        """Constructor for the ChannelModel class"""

        # Initialize members of the class
        self.name = name
        self.url = url
        self.mtype = mtype
        self.mc_enabled = mc_enabled
        self.contract_credentials = contract_credentials
        self.contract_facets = contract_facets
        self.posting_requirements = posting_requirements
        self.manual_setup_required = manual_setup_required
        self.setup_instructions = setup_instructions
        self.feed_url = feed_url

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

        name = dictionary.get('name')
        url = dictionary.get('url')
        mtype = dictionary.get('type')
        mc_enabled = dictionary.get('mc_enabled')
        contract_credentials = None
        if dictionary.get('contract_credentials') is not None:
            contract_credentials = [ContractCredentialModel.from_dictionary(x) for x in dictionary.get('contract_credentials')]
        contract_facets = dictionary.get('contract_facets')
        posting_requirements = None
        if dictionary.get('posting_requirements') is not None:
            posting_requirements = [FacetModel.from_dictionary(x) for x in dictionary.get('posting_requirements')]
        manual_setup_required = dictionary.get('manual_setup_required')
        setup_instructions = dictionary.get('setup_instructions')
        feed_url = dictionary.get('feed_url')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   url,
                   mtype,
                   mc_enabled,
                   contract_credentials,
                   contract_facets,
                   posting_requirements,
                   manual_setup_required,
                   setup_instructions,
                   feed_url,
                   dictionary)
