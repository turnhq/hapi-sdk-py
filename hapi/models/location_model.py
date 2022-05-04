# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class LocationModel(object):

    """Implementation of the 'Location' model.

    Location(id, canonical_name, desq_name_en, desq_country_code,
    country_code, mapbox_id, mapbox_text, mapbox_placename, mapbox_context,
    mapbox_place_type, mapbox_shortcode, mapbox_within)

    Attributes:
        id (float): TODO: type description here.
        fully_qualified_place_name (string): TODO: type description here.
        canonical_name (string): TODO: type description here.
        bounding_box (list of float): TODO: type description here.
        area (float): TODO: type description here.
        place_type (PlaceTypeEnum): TODO: type description here.
        within (LocationModel): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "fully_qualified_place_name": 'fully_qualified_place_name',
        "canonical_name": 'canonical_name',
        "bounding_box": 'bounding_box',
        "area": 'area',
        "place_type": 'place_type',
        "within": 'within'
    }

    def __init__(self,
                 id=None,
                 fully_qualified_place_name=None,
                 canonical_name=None,
                 bounding_box=None,
                 area=None,
                 place_type=None,
                 within=None,
                 additional_properties={}):
        """Constructor for the LocationModel class"""

        # Initialize members of the class
        self.id = id
        self.fully_qualified_place_name = fully_qualified_place_name
        self.canonical_name = canonical_name
        self.bounding_box = bounding_box
        self.area = area
        self.place_type = place_type
        self.within = within

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

        id = dictionary.get('id')
        fully_qualified_place_name = dictionary.get('fully_qualified_place_name')
        canonical_name = dictionary.get('canonical_name')
        bounding_box = dictionary.get('bounding_box')
        area = dictionary.get('area')
        place_type = dictionary.get('place_type')
        within = LocationModel.from_dictionary(dictionary.get('within')) if dictionary.get('within') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   fully_qualified_place_name,
                   canonical_name,
                   bounding_box,
                   area,
                   place_type,
                   within,
                   dictionary)
