# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.autocomplete_model import AutocompleteModel
from hapi.models.facet_option_model import FacetOptionModel
from hapi.models.facet_rule_model import FacetRuleModel


class FacetModel(object):

    """Implementation of the 'Facet' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the Facet. To be used as a key when
            ordering a Campaign, under the
            `orderedProductsSpecs.postingRequirements` key.
        label (string): The user facing label
        sort (string): The order in the list of vacancy fields to be displayed
            to the user when posting. Facets with lower `sort` values should
            be displayed first.
        required (bool): Whether the Facet is required when ordering a
            Campaign.
        mtype (TypeEnum): The type of UI and data structure to be used to
            input and store values for this Facet.
        options (list of FacetOptionModel): list of choices for this Facet's
            value.
        rules (list of FacetRuleModel): special validation rules that apply
            for this Facet's value
        autocomplete (AutocompleteModel): Used for Facets whose value choices
            need to be fetched through an additional call to the [List
            autocomplete values for posting
            requirements](https://vonq.stoplight.io/docs/hapi/b3A6MzM2MDEzODk-l
            ist-autocomplete-values-for-posting-requirement) endpoint.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "label": 'label',
        "sort": 'sort',
        "required": 'required',
        "mtype": 'type',
        "options": 'options',
        "rules": 'rules',
        "autocomplete": 'autocomplete'
    }

    def __init__(self,
                 name=None,
                 label=None,
                 sort=None,
                 required=None,
                 mtype=None,
                 options=None,
                 rules=None,
                 autocomplete=None,
                 additional_properties={}):
        """Constructor for the FacetModel class"""

        # Initialize members of the class
        self.name = name
        self.label = label
        self.sort = sort
        self.required = required
        self.mtype = mtype
        self.options = options
        self.rules = rules
        self.autocomplete = autocomplete

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
        label = dictionary.get('label')
        sort = dictionary.get('sort')
        required = dictionary.get('required')
        mtype = dictionary.get('type')
        options = None
        if dictionary.get('options') is not None:
            options = [FacetOptionModel.from_dictionary(x) for x in dictionary.get('options')]
        rules = None
        if dictionary.get('rules') is not None:
            rules = [FacetRuleModel.from_dictionary(x) for x in dictionary.get('rules')]
        autocomplete = AutocompleteModel.from_dictionary(dictionary.get('autocomplete')) if dictionary.get('autocomplete') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   label,
                   sort,
                   required,
                   mtype,
                   options,
                   rules,
                   autocomplete,
                   dictionary)
