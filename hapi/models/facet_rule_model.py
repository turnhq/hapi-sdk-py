# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class FacetRuleModel(object):

    """Implementation of the 'FacetRule' model.

    TODO: type model description here.

    Attributes:
        rule (RuleEnum): TODO: type description here.
        data (string): the value used for the rule

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rule": 'rule',
        "data": 'data'
    }

    def __init__(self,
                 rule=None,
                 data=None,
                 additional_properties={}):
        """Constructor for the FacetRuleModel class"""

        # Initialize members of the class
        self.rule = rule
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

        rule = dictionary.get('rule')
        data = dictionary.get('data')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(rule,
                   data,
                   dictionary)
