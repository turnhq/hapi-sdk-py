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
from hapi.models.product_model import ProductModel
from hapi.models.products_delivery_time_model import ProductsDeliveryTimeModel
from hapi.exceptions.api_exception import APIException
import json


class PortfolioController(BaseController):

    """A Controller to access Endpoints in the hapi API."""
    def __init__(self, config, auth_managers):
        super(PortfolioController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def search_products(self,
                        limit=None,
                        offset=None,
                        include_location_id=None,
                        exact_location_id=None,
                        job_function_id=None,
                        job_title_id=None,
                        industry_id=None,
                        duration_from=None,
                        duration_to=None,
                        name=None,
                        currency=None,
                        sort_by='relevant',
                        recommended=None,
                        mc_enabled=None,
                        accept_language=None,
                        exclude_recommended=False):
        """Does a GET request to /products/search/.

        For a detailed tutorial on how to get started with portfolio search
        v2, check out our [Quickstart
        Tutorial](https://pkb.stoplight.io/docs/search/docs/Tutorial.md).
        For an implementation demo of the product search experience, check out
        our [Developer Portal](http://vonq.io/pkb).
        This endpoint exposes a list of Products with the options to search by
        Location, Job Title, Job Function and Industry.
        Products are ranked by their relevancy to the search terms.
        Optionally, products can filtered by Location.
        Values for each parameter can be fetched by calling the other
        endpoints in this section.
        Calling this endpoint will guarantee that the Products you see are
        configured for you as our Partner.
        Besides the default English, German and Dutch result translations can
        be requested by specifying an `Accept-Language: [de|nl]` header.

        Args:
            limit (int, optional): Number of results to return per page.
            offset (int, optional): The initial index from which to return the
                results.
            include_location_id (list of string, optional): Id for a Location
                to search products against. If no exact matches exist, search
                will be expanded to the Location's region and country.
                Optionally, a (comma-separated) array of values can be passed.
                Passing multiple values increases the number of search
                results.
            exact_location_id (string, optional): Match only products
                specifically assigned to a Location.
            job_function_id (string, optional): Job Function id. Not to be
                used in conjunction with a Job Title id.
            job_title_id (string, optional): Job title id
            industry_id (list of string, optional): Industry Id
            duration_from (string, optional): Match only products with a
                duration more or equal than a certain number of days
            duration_to (string, optional): Match only products with a
                duration up to a certain number of days
            name (string, optional): Search text for a product name
            currency (string, optional): ISO-4217 code for a currency
            sort_by (SortByEnum, optional): Which products to show first.
                Defaults to 'relevant'
            recommended (bool, optional): Whether to display a list of
                recommended products for the search parameters. If true,
                returns a limited list of products for the types: Job board,
                social media, publication and community.
            mc_enabled (bool, optional): Can be used to filter for products
                that are linked to a channel enabled for My Contracts orders
            accept_language (AcceptLanguageEnum, optional): TODO: type
                description here.
            exclude_recommended (bool, optional): Exclude recommended products
                from search results. Cannot be used in combination with
                'recommended'.

        Returns:
            list of ProductModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('search_products called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for search_products.')
            _url_path = '/products/search/'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'limit': limit,
                'offset': offset,
                'includeLocationId': include_location_id,
                'exactLocationId': exact_location_id,
                'jobFunctionId': job_function_id,
                'jobTitleId': job_title_id,
                'industryId': industry_id,
                'durationFrom': duration_from,
                'durationTo': duration_to,
                'name': name,
                'currency': currency,
                'sortBy': sort_by,
                'recommended': recommended,
                'mcEnabled': mc_enabled,
                'excludeRecommended': exclude_recommended
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder,
                _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for search_products.')
            _headers = {
                'accept': 'application/json',
                'Accept-Language': accept_language
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for search_products.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'search_products')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for search_products.')
            if _response.status_code == 400:
                raise APIException('', _response)
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def retrieve_single_product(self,
                                product_id,
                                accept_language=None):
        """Does a GET request to /products/single/{product_id}/.

        Sometimes you already have access to the Identification code of any
        particular Product and you want to retrieve the most up-to-date
        information about it.
        Besides the default English, German and Dutch result translations can
        be requested by specifying an `Accept-Language: [de|nl]` header.

        Args:
            product_id (string): TODO: type description here.
            accept_language (AcceptLanguageEnum, optional): TODO: type
                description here.

        Returns:
            ProductModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('retrieve_single_product called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for retrieve_single_product.')
            _url_path = '/products/single/{product_id}/'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'product_id': {'value': product_id, 'encode': True}
            })
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for retrieve_single_product.')
            _headers = {
                'accept': 'application/json',
                'Accept-Language': accept_language
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for retrieve_single_product.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'retrieve_single_product')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def retrieve_multiple_products(self,
                                   products_ids,
                                   accept_language=None):
        """Does a GET request to /products/multiple/{products_ids}/.

        Sometimes you already have access to the Identification codes of more
        than one Product and you want to retrieve the most up-to-date
        information about them.
        Besides the default English, German and Dutch result translations can
        be requested by specifying an `Accept-Language: [de|nl]` header.

        Args:
            products_ids (list of string): TODO: type description here.
            accept_language (AcceptLanguageEnum, optional): TODO: type
                description here.

        Returns:
            list of ProductModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('retrieve_multiple_products called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for retrieve_multiple_products.')
            _url_path = '/products/multiple/{products_ids}/'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'products_ids': {'value': products_ids, 'encode': True}
            })
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for retrieve_multiple_products.')
            _headers = {
                'accept': 'application/json',
                'Accept-Language': accept_language
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for retrieve_multiple_products.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'retrieve_multiple_products')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def calculate_order_delivery_time(self,
                                      products_ids):
        """Does a GET request to /products/delivery-time/{products_ids}/.

        This endpoint calculates total number of days to process and setup a
        campaign containing a list of Products, given a comma-separated list
        of their ids.

        Args:
            products_ids (list of string): TODO: type description here.

        Returns:
            list of ProductsDeliveryTimeModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('calculate_order_delivery_time called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for calculate_order_delivery_time.')
            _url_path = '/products/delivery-time/{products_ids}/'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'products_ids': {'value': products_ids, 'encode': True}
            })
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for calculate_order_delivery_time.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for calculate_order_delivery_time.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'calculate_order_delivery_time')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
