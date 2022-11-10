# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import logging
from hapi.api_helper import APIHelper
from hapi.configuration import Server
from hapi.controllers.base_controller import BaseController
from hapi.models.job_function_model import JobFunctionModel
from hapi.models.job_title_model import JobTitleModel
from hapi.models.location_model import LocationModel
from hapi.models.industry_model import IndustryModel
from hapi.models.education_level_model import EducationLevelModel
from hapi.models.seniority_model import SeniorityModel
import json

class TaxonomyController(BaseController):

    """A Controller to access Endpoints in the hapi API."""
    def __init__(self, config, auth_managers):
        super(TaxonomyController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def retrieve_job_functions_tree(self,
                                    accept_language=None):
        """Does a GET request to /products/job-functions/.

        This endpoint returns a tree-like structure of supported Job Functions
        that can be used to search for Products.
        Use the `id` key of any Job Function in the response to search for a
        Product.
        Each Job Function is associated with [**`Job
        Titles`**](b3A6MzM0NDA3MzY-job-titles) in a one-to-many fashion.
        Besides the default English, German and Dutch result translations can
        be requested by specifying an `Accept-Language: [de|nl]` header.

        Args:
            accept_language (AcceptLanguageEnum, optional): TODO: type
                description here.

        Returns:
            list of JobFunctionModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('retrieve_job_functions_tree called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for retrieve_job_functions_tree.')
            _url_path = '/products/job-functions/'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for retrieve_job_functions_tree.')
            _headers = {
                'accept': 'application/json',
                'Accept-Language': accept_language
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for retrieve_job_functions_tree.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'retrieve_job_functions_tree')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def search_job_titles(self,
                          text,
                          limit=None,
                          offset=None,
                          accept_language=None):
        """Does a GET request to /products/job-titles/.

        This endpoint takes any text as input and returns a list of supported
        Job Titles matching the query, ordered by popularity.
        Use the `id` key of each object in the response to search for a
        Product.
        Currently, we support 4,000 job titles for each of the following
        languages: English, Dutch and German.
        Each Job Title is associated with a [**`Job
        Function`**](b3A6MzM0NDA3MzU-job-functions) in a many-to-one fashion.
        Besides the default English, German and Dutch result translations can
        be requested by specifying an `Accept-Language: [de|nl]` header.

        Args:
            text (string): Search text for a job title name
            limit (float, optional): Number of results to return per page.
            offset (float, optional): The initial index from which to return
                the results.
            accept_language (AcceptLanguageEnum, optional): TODO: type
                description here.

        Returns:
            list of JobTitleModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_job_titles called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for search_job_titles.')
            _url_path = '/products/job-titles/'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'text': text,
                'limit': limit,
                'offset': offset
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder,
                _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for search_job_titles.')
            _headers = {
                'accept': 'application/json',
                'Accept-Language': accept_language
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for search_job_titles.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'search_job_titles')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def search_locations(self,
                         text):
        """Does a GET request to /products/location/search/.

        This endpoint takes any text as input and returns a list of Locations
        matching the query, ordered by popularity.
        Each response will include the entire world as a Location, even no
        Locations match the text query.
        Use the `id` key of each object in the response to search for a
        Product.
        Supports text input in English, Dutch and German.

        Args:
            text (string): Search text for a location name in either English,
                Dutch, German, French and Italian. Partial recognition of 20
                other languages.

        Returns:
            list of LocationModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_locations called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for search_locations.')
            _url_path = '/products/location/search/'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'text': text
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder,
                _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for search_locations.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for search_locations.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'search_locations')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def list_industries(self,
                        limit=None,
                        offset=None,
                        accept_language=None):
        """Does a GET request to /products/industries/.

        This endpoint returns a list of supported industry names that can be
        used to search for products. Results are ordered alphabetically.
        Use the `id` key of any Industry in the response to search for a
        product.
        Besides the default English, German and Dutch result translations can
        be requested by specifying an `Accept-Language: [de|nl]` header.

        Args:
            limit (float, optional): Number of results to return per page.
            offset (float, optional): The initial index from which to return
                the results.
            accept_language (AcceptLanguageEnum, optional): TODO: type
                description here.

        Returns:
            list of IndustryModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_industries called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for list_industries.')
            _url_path = '/products/industries/'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'limit': limit,
                'offset': offset
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder,
                _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for list_industries.')
            _headers = {
                'accept': 'application/json',
                'Accept-Language': accept_language
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for list_industries.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'list_industries')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def retrieve_education_levels(self):
        """Does a GET request to /taxonomy/education-levels.

        Retrieve all Education Level possible values.

        Returns:
            list of EducationLevelModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('retrieve_education_levels called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for retrieve_education_levels.')
            _url_path = '/taxonomy/education-levels'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for retrieve_education_levels.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for retrieve_education_levels.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'retrieve_education_levels')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def retrieve_seniorities(self):
        """Does a GET request to /taxonomy/seniority.

        Retrieve all Seniority possible values.

        Returns:
            list of SeniorityModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('retrieve_seniorities called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for retrieve_seniorities.')
            _url_path = '/taxonomy/seniority'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for retrieve_seniorities.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for retrieve_seniorities.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'retrieve_seniorities')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
