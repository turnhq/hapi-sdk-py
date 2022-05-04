# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.target_group_element_model import TargetGroupElementModel


class TargetGroupModel(object):

    """Implementation of the 'TargetGroup' model.

    TODO: type model description here.

    Attributes:
        education_level (list of TargetGroupElementModel): Education Level
            required by the Candidate. You can specify only one value.
        seniority (list of TargetGroupElementModel): Seniority Level expected
            by the Candidate. You can specify only one value.
        industry (list of TargetGroupElementModel): The Industry related to
            the Position open. You can specify only one value.
        job_category (list of TargetGroupElementModel): Job Category indicates
            the type of Position that's open. You can specify only one value.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "education_level": 'educationLevel',
        "seniority": 'seniority',
        "industry": 'industry',
        "job_category": 'jobCategory'
    }

    def __init__(self,
                 education_level=None,
                 seniority=None,
                 industry=None,
                 job_category=None,
                 additional_properties={}):
        """Constructor for the TargetGroupModel class"""

        # Initialize members of the class
        self.education_level = education_level
        self.seniority = seniority
        self.industry = industry
        self.job_category = job_category

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

        education_level = None
        if dictionary.get('educationLevel') is not None:
            education_level = [TargetGroupElementModel.from_dictionary(x) for x in dictionary.get('educationLevel')]
        seniority = None
        if dictionary.get('seniority') is not None:
            seniority = [TargetGroupElementModel.from_dictionary(x) for x in dictionary.get('seniority')]
        industry = None
        if dictionary.get('industry') is not None:
            industry = [TargetGroupElementModel.from_dictionary(x) for x in dictionary.get('industry')]
        job_category = None
        if dictionary.get('jobCategory') is not None:
            job_category = [TargetGroupElementModel.from_dictionary(x) for x in dictionary.get('jobCategory')]
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(education_level,
                   seniority,
                   industry,
                   job_category,
                   dictionary)
