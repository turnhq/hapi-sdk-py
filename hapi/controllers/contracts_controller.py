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
from hapi.models.list_channels_response_model import ListChannelsResponseModel
from hapi.models.channel_model import ChannelModel
from hapi.models.list_contracts_response_model import ListContractsResponseModel
from hapi.models.create_contract_response_model import CreateContractResponseModel
from hapi.models.contract_model import ContractModel
from hapi.models.multiple_contracts_response_model import MultipleContractsResponseModel
from hapi.models.autocomplete_values_response_model import AutocompleteValuesResponseModel
from hapi.exceptions.api_exception import APIException
import json


class ContractsController(BaseController):

    """A Controller to access Endpoints in the hapi API."""
    def __init__(self, config, auth_managers):
        super(ContractsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def list_channels(self,
                      search=None,
                      limit=None,
                      offset=None,
                      accept_language=None):
        """Does a GET request to /products/channels/mocs/.

        This endpoint exposes a list of channels with support for contracts.
        For all of the required details for creating a contract or a campaign
        for each channel, please call the "Retrieve details for channel with
        support for contracts".

        Args:
            search (string, optional): A search term.
            limit (int, optional): Number of results to return per page.
            offset (int, optional): The initial index from which to return the
                results.
            accept_language (AcceptLanguageEnum, optional): The language the
                client prefers.

        Returns:
            ListChannelsResponseModel: Response from the API. Paginated list
                of channels.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_channels called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for list_channels.')
            _url_path = '/products/channels/mocs/'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'search': search,
                'limit': limit,
                'offset': offset
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder,
                _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for list_channels.')
            _headers = {
                'accept': 'application/json',
                'Accept-Language': accept_language
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for list_channels.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'list_channels')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def retrieve_channel(self,
                         channel_id,
                         accept_language=None):
        """Does a GET request to /products/channels/mocs/{channel_id}.

        This endpoint exposes the details of a channel with support for
        contracts,as well as all the required details for creating a contract
        or a campaign for each channel.

        Args:
            channel_id (string): ID of the channel
            accept_language (AcceptLanguageEnum, optional): The language the
                client prefers.

        Returns:
            ChannelModel: Response from the API. Channel details

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('retrieve_channel called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for retrieve_channel.')
            _url_path = '/products/channels/mocs/{channel_id}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'channel_id': {'value': channel_id, 'encode': True}
            })
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for retrieve_channel.')
            _headers = {
                'accept': 'application/json',
                'Accept-Language': accept_language
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for retrieve_channel.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'customerId', 'token')
    
            _response = self.execute_request(_request, name = 'retrieve_channel')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def list_contracts(self,
                       x_customer_id,
                       limit=None,
                       offset=None):
        """Does a GET request to /contracts/.

        This endpoint exposes a list of contract available to a particular
        customer.

        Args:
            x_customer_id (string): An identifier for the remote customer
            limit (float, optional): Amount of contracts returned
            offset (float, optional): Starting point

        Returns:
            ListContractsResponseModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_contracts called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for list_contracts.')
            _url_path = '/contracts/'
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
            self.logger.info('Preparing headers for list_contracts.')
            _headers = {
                'accept': 'application/json',
                'X-Customer-Id': x_customer_id
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for list_contracts.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token', 'customerId')
    
            _response = self.execute_request(_request, name = 'list_contracts')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_contract(self,
                        x_customer_id,
                        body):
        """Does a POST request to /contracts/.

        This endpoint creates a new customer contract. It requires a reference
        to a channel, a credential payload, and the facets set for the
        contracted product.
        HAPI doesn't support contract editing, because job boards require the
        same credentials to be able to delete already posted jobs via that
        contract at a later moment. Otherwise, deleting jobs would not be
        possible. To edit contract credentials, the credentials need to be
        deleted first, and then recreated. When deleted, all corresponding
        jobs can't be deleted anymore

        Args:
            x_customer_id (string): An identifier for the remote customer
            body (PostContractModel): TODO: type description here.

        Returns:
            CreateContractResponseModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_contract called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_contract.')
            _url_path = '/contracts/'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_contract.')
            _headers = {
                'accept': 'application/json',
                'X-Customer-Id': x_customer_id,
                'Content-Type': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_contract.')
            _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'create_contract')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_contract.')
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def delete_contract(self,
                        contract_id,
                        x_customer_id):
        """Does a DELETE request to /contracts/{contract_id}/.

        This endpoint deletes a contract. 
         HAPI doesn't support contract editing, because job boards require the
         same credentials to be able to delete already posted jobs via that
         contract at a later moment. Otherwise, deleting jobs would not be
         possible. To edit contract credentials, the credentials need to be
         deleted first, and then recreated. When deleted, all corresponding
         jobs can't be deleted anymore

        Args:
            contract_id (string): TODO: type description here.
            x_customer_id (string): An identifier for the remote customer

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_contract called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for delete_contract.')
            _url_path = '/contracts/{contract_id}/'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'contract_id': {'value': contract_id, 'encode': True}
            })
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for delete_contract.')
            _headers = {
                'X-Customer-Id': x_customer_id
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for delete_contract.')
            _request = self.config.http_client.delete(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token', 'customerId')
    
            _response = self.execute_request(_request, name = 'delete_contract')
            self.validate_response(_response)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def retrieve_contract(self,
                          contract_id,
                          x_customer_id):
        """Does a GET request to /contracts/single/{contract_id}/.

        This endpoint retrieves the detail for a customer contract. It
        contains a reference to a channel, an (encrypted) credential payload,
        and the facets set for the My Contracts product.

        Args:
            contract_id (string): TODO: type description here.
            x_customer_id (string): An identifier for the remote customer

        Returns:
            ContractModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('retrieve_contract called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for retrieve_contract.')
            _url_path = '/contracts/single/{contract_id}/'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'contract_id': {'value': contract_id, 'encode': True}
            })
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for retrieve_contract.')
            _headers = {
                'accept': 'application/json',
                'X-Customer-Id': x_customer_id
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for retrieve_contract.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token', 'customerId')
    
            _response = self.execute_request(_request, name = 'retrieve_contract')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def retrieve_multiple_contracts(self,
                                    contracts_ids,
                                    limit=None,
                                    offset=None):
        """Does a GET request to /contracts/multiple/{contracts_ids}/.

        This endpoint exposes a list of multiple contracts, if available to a
        specific customer.

        Args:
            contracts_ids (list of string): TODO: type description here.
            limit (float, optional): Amount of contracts returned
            offset (float, optional): Starting point

        Returns:
            MultipleContractsResponseModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('retrieve_multiple_contracts called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for retrieve_multiple_contracts.')
            _url_path = '/contracts/multiple/{contracts_ids}/'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'contracts_ids': {'value': contracts_ids, 'encode': True}
            })
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
            self.logger.info('Preparing headers for retrieve_multiple_contracts.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for retrieve_multiple_contracts.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token', 'customerId')
    
            _response = self.execute_request(_request, name = 'retrieve_multiple_contracts')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def list_autocomplete_values(self,
                                 channel_id,
                                 posting_requirement_name,
                                 body):
        """Does a POST request to /contracts/posting-requirements/{channel_id}/{posting-requirement-name}/.

        This endpoint exposes autocomplete items given a `channel_id` and a
        posting requirement name.

        Args:
            channel_id (float): channel_id (number, required)
            posting_requirement_name (string): TODO: type description here.
            body (FacetAutocompleteModel): TODO: type description here.

        Returns:
            list of AutocompleteValuesResponseModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_autocomplete_values called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for list_autocomplete_values.')
            _url_path = '/contracts/posting-requirements/{channel_id}/{posting-requirement-name}/'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'channel_id': {'value': channel_id, 'encode': True},
                'posting-requirement-name': {'value': posting_requirement_name, 'encode': True}
            })
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for list_autocomplete_values.')
            _headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for list_autocomplete_values.')
            _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token', 'customerId')
    
            _response = self.execute_request(_request, name = 'list_autocomplete_values')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for list_autocomplete_values.')
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
