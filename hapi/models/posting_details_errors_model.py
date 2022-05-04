# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.organization_model import OrganizationModel
from hapi.models.salary_indication_model import SalaryIndicationModel
from hapi.models.weekly_working_hours_model import WeeklyWorkingHoursModel
from hapi.models.working_location_model import WorkingLocationModel


class PostingDetailsErrorsModel(object):

    """Implementation of the 'PostingDetailsErrors' model.

    TODO: type model description here.

    Attributes:
        title (list of string): TODO: type description here.
        description (list of string): TODO: type description here.
        years_of_experience (list of string): TODO: type description here.
        employment_type (list of string): TODO: type description here.
        organization (OrganizationModel): TODO: type description here.
        working_location (WorkingLocationModel): TODO: type description here.
        weekly_working_hours (WeeklyWorkingHoursModel): TODO: type description
            here.
        salary_indication (SalaryIndicationModel): TODO: type description
            here.
        job_page_url (list of string): TODO: type description here.
        application_url (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title": 'title',
        "description": 'description',
        "years_of_experience": 'yearsOfExperience',
        "employment_type": 'employmentType',
        "organization": 'organization',
        "working_location": 'workingLocation',
        "weekly_working_hours": 'weeklyWorkingHours',
        "salary_indication": 'salaryIndication',
        "job_page_url": 'jobPageUrl',
        "application_url": 'applicationUrl'
    }

    def __init__(self,
                 title=None,
                 description=None,
                 years_of_experience=None,
                 employment_type=None,
                 organization=None,
                 working_location=None,
                 weekly_working_hours=None,
                 salary_indication=None,
                 job_page_url=None,
                 application_url=None,
                 additional_properties={}):
        """Constructor for the PostingDetailsErrorsModel class"""

        # Initialize members of the class
        self.title = title
        self.description = description
        self.years_of_experience = years_of_experience
        self.employment_type = employment_type
        self.organization = organization
        self.working_location = working_location
        self.weekly_working_hours = weekly_working_hours
        self.salary_indication = salary_indication
        self.job_page_url = job_page_url
        self.application_url = application_url

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
        description = dictionary.get('description')
        years_of_experience = dictionary.get('yearsOfExperience')
        employment_type = dictionary.get('employmentType')
        organization = OrganizationModel.from_dictionary(dictionary.get('organization')) if dictionary.get('organization') else None
        working_location = WorkingLocationModel.from_dictionary(dictionary.get('workingLocation')) if dictionary.get('workingLocation') else None
        weekly_working_hours = WeeklyWorkingHoursModel.from_dictionary(dictionary.get('weeklyWorkingHours')) if dictionary.get('weeklyWorkingHours') else None
        salary_indication = SalaryIndicationModel.from_dictionary(dictionary.get('salaryIndication')) if dictionary.get('salaryIndication') else None
        job_page_url = dictionary.get('jobPageUrl')
        application_url = dictionary.get('applicationUrl')
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(title,
                   description,
                   years_of_experience,
                   employment_type,
                   organization,
                   working_location,
                   weekly_working_hours,
                   salary_indication,
                   job_page_url,
                   application_url,
                   dictionary)
