# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from hapi.models.posting_contact_info_model import PostingContactInfoModel
from hapi.models.posting_organization_model import PostingOrganizationModel
from hapi.models.posting_salary_indication_model import PostingSalaryIndicationModel
from hapi.models.posting_weekly_working_hours_model import PostingWeeklyWorkingHoursModel
from hapi.models.posting_working_location_model import PostingWorkingLocationModel


class PostingDetailsModel(object):

    """Implementation of the 'PostingDetails' model.

    TODO: type model description here.

    Attributes:
        title (string): The title of the posting across the different Channels
            where the posting is going to be published.
        description (string): Full description of the job posting, including
            all possible sections  **Allowed tags:** `a[href|target], em, b,
            br, strong, i, li, ol, p, ul`
        organization (PostingOrganizationModel): TODO: type description here.
        working_location (PostingWorkingLocationModel): TODO: type description
            here.
        contact_info (PostingContactInfoModel): Contact is whom to contact
            about the job. This may be part of the posting info for candidates
            to know whom they can reach out to learn more about the vacancy.
        years_of_experience (float): Numbers of years of experience required
            for this position
        employment_type (EmploymentTypeEnum): The type of employment of the
            posting, whether it's a permanent position or a fixed time
            position
        weekly_working_hours (PostingWeeklyWorkingHoursModel): TODO: type
            description here.
        salary_indication (PostingSalaryIndicationModel): TODO: type
            description here.
        job_page_url (string): Link to the page with the description of the
            job
        application_url (string): Link to the page where the candidate needs
            to be directed when applying for a position

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title": 'title',
        "description": 'description',
        "organization": 'organization',
        "working_location": 'workingLocation',
        "years_of_experience": 'yearsOfExperience',
        "employment_type": 'employmentType',
        "weekly_working_hours": 'weeklyWorkingHours',
        "salary_indication": 'salaryIndication',
        "job_page_url": 'jobPageUrl',
        "application_url": 'applicationUrl',
        "contact_info": 'contactInfo'
    }

    def __init__(self,
                 title=None,
                 description=None,
                 organization=None,
                 working_location=None,
                 years_of_experience=None,
                 employment_type=None,
                 weekly_working_hours=None,
                 salary_indication=None,
                 job_page_url=None,
                 application_url=None,
                 contact_info=None,
                 additional_properties={}):
        """Constructor for the PostingDetailsModel class"""

        # Initialize members of the class
        self.title = title
        self.description = description
        self.organization = organization
        self.working_location = working_location
        self.contact_info = contact_info
        self.years_of_experience = years_of_experience
        self.employment_type = employment_type
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
        organization = PostingOrganizationModel.from_dictionary(dictionary.get('organization')) if dictionary.get('organization') else None
        working_location = PostingWorkingLocationModel.from_dictionary(dictionary.get('workingLocation')) if dictionary.get('workingLocation') else None
        years_of_experience = dictionary.get('yearsOfExperience')
        employment_type = dictionary.get('employmentType')
        weekly_working_hours = PostingWeeklyWorkingHoursModel.from_dictionary(dictionary.get('weeklyWorkingHours')) if dictionary.get('weeklyWorkingHours') else None
        salary_indication = PostingSalaryIndicationModel.from_dictionary(dictionary.get('salaryIndication')) if dictionary.get('salaryIndication') else None
        job_page_url = dictionary.get('jobPageUrl')
        application_url = dictionary.get('applicationUrl')
        contact_info = PostingContactInfoModel.from_dictionary(dictionary.get('contactInfo')) if dictionary.get('contactInfo') else None
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(title,
                   description,
                   organization,
                   working_location,
                   years_of_experience,
                   employment_type,
                   weekly_working_hours,
                   salary_indication,
                   job_page_url,
                   application_url,
                   contact_info,
                   dictionary)
