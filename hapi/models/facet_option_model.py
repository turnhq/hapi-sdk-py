# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.facet_option_show_facets_model import FacetOptionShowFacetsModel


class FacetOptionModel(object):

    """Implementation of the 'FacetOption' model.

    TODO: type model description here.

    Attributes:
        default (string): Whether the option should be the default choice when
            rendering the SELECT.
        key (string): The value to be used when setting the value of the facet
            when this option is selected.
        label (string): The option's user-friendly label
        sort (string): The order of the option in the list of options. lower
            value means higher rank.
        show (list of FacetOptionShowFacetsModel): References to Facets that
            becomes required when this option is selected

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default": 'default',
        "key": 'key',
        "label": 'label',
        "sort": 'sort',
        "show": 'show'
    }

    def __init__(self,
                 default=None,
                 key=None,
                 label=None,
                 sort=None,
                 show=None,
                 additional_properties={}):
        """Constructor for the FacetOptionModel class"""

        # Initialize members of the class
        self.default = default
        self.key = key
        self.label = label
        self.sort = sort
        self.show = show

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

        default = dictionary.get('default')
        key = dictionary.get('key')
        label = dictionary.get('label')
        sort = dictionary.get('sort')
        show = None
        if dictionary.get('show') is not None:
            show = [FacetOptionShowFacetsModel.from_dictionary(x) for x in dictionary.get('show')]
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(default,
                   key,
                   label,
                   sort,
                   show,
                   dictionary)
