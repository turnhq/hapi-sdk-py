# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TargetGroupElementModel(object):

    """Implementation of the 'TargetGroupElement' model.

    TODO: type model description here.

    Attributes:
        description (string): The vonq name for this target group element
        vonq_id (string): The Vonq ID representing this concept, as indicated
            in the [**`Taxonomy
            Endpoints`**](#reference/experimental-products-search)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "vonq_id": 'vonqId'
    }

    def __init__(self,
                 description=None,
                 vonq_id=None,
                 additional_properties={}):
        """Constructor for the TargetGroupElementModel class"""

        # Initialize members of the class
        self.description = description
        self.vonq_id = vonq_id

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

        description = dictionary.get('description')
        vonq_id = dictionary.get('vonqId')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(description,
                   vonq_id,
                   dictionary)
