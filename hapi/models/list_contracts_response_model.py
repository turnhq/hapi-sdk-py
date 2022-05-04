# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.contract_model import ContractModel


class ListContractsResponseModel(object):

    """Implementation of the 'ListContractsResponse' model.

    TODO: type model description here.

    Attributes:
        count (float): count of elements in results
        previous (string): link to get previous results
        next (string): link to get next results
        results (list of ContractModel): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "previous": 'previous',
        "next": 'next',
        "results": 'results'
    }

    def __init__(self,
                 count=None,
                 previous=None,
                 next=None,
                 results=None,
                 additional_properties={}):
        """Constructor for the ListContractsResponseModel class"""

        # Initialize members of the class
        self.count = count
        self.previous = previous
        self.next = next
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
        previous = dictionary.get('previous')
        next = dictionary.get('next')
        results = None
        if dictionary.get('results') is not None:
            results = [ContractModel.from_dictionary(x) for x in dictionary.get('results')]
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(count,
                   previous,
                   next,
                   results,
                   dictionary)
