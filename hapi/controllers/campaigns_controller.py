# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import json
import logging
from hapi.api_helper import APIHelper
from hapi.configuration import Server
from hapi.controllers.base_controller import BaseController
from hapi.models.order_campaign_success_response_model import OrderCampaignSuccessResponseModel
from hapi.models.result_set_1_model import ResultSet1Model
from hapi.models.list_campaign_response_model import ListCampaignResponseModel
from hapi.models.check_campaign_statusresponse_model import CheckCampaignStatusresponseModel
from hapi.models.take_campaign_offline_response_model import TakeCampaignOfflineResponseModel
from hapi.exceptions.order_campaign_error_response_exception import OrderCampaignErrorResponseException
from hapi.exceptions.take_campaign_offline_error_response_2_exception import TakeCampaignOfflineErrorResponse2Exception
from hapi.exceptions.take_campaign_offline_error_response_exception import TakeCampaignOfflineErrorResponseException


class CampaignsController(BaseController):

    """A Controller to access Endpoints in the hapi API."""
    def __init__(self, config, auth_managers):
        super(CampaignsController, self).__init__(config, auth_managers)
        self.logger = logging.getLogger(__name__)

    def order_campaign(self,
                       body,
                       company_id=None,
                       limit=None,
                       offset=None,
                       x_customer_id=None):
        """Does a POST request to /campaigns/order.

        Once your Customer has decided on a list of Channels they would like
        to buy, you can send the list along with
        publishing information as a `POST` request in order to create a
        `Campaign`. In return, you'll receive
        the id of the newly created `Campaign` along with the URL where you
        can access that Campaign information.
        For "My Contracts" type of Products, there is no expiration. The
        vacancy can be taken offline either by the job board or manually, by
        calling the "[Take a campaign
        offline](https://vonq.stoplight.io/docs/hapi/b3A6MzM0NDA3MzQ-take-a-cam
        paign-offline)" endpoint.
        #### Target group
        You should use the following endpoints for the target group
        information:
        - [**`Industry`**](b3A6MzM0NDA3Mzg-industry-names)
        - [**`Job Function`**](b3A6MzM0NDA3MzU-job-functions)
        - [**`Education
        Level`**](b3A6MzM0NDA3Mzk-retrieve-education-level-taxonomy)
        - [**`Seniority`**](b3A6MzM0NDA3NDA-retrieve-seniority-taxonomy)

        Args:
            body (CampaignOrderModel): TODO: type description here.
            company_id (string, optional): TODO: type description here.
            limit (string, optional): TODO: type description here.
            offset (string, optional): TODO: type description here.
            x_customer_id (string, optional): The ID of the end-user creating
                the order. Only required if you are using HAPI Job Post and
                creating orders with contracts.

        Returns:
            OrderCampaignSuccessResponseModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('order_campaign called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for order_campaign.')
            _url_path = '/campaigns/order'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'companyId': company_id,
                'limit': limit,
                'offset': offset
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder,
                _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for order_campaign.')
            _headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json',
                'X-Customer-Id': x_customer_id
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for order_campaign.')
            _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'order_campaign')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for order_campaign.')
            if _response.status_code == 400:
                raise OrderCampaignErrorResponseException('', _response)
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def list_campaigns(self,
                       company_id,
                       limit=None,
                       offset=None):
        """Does a GET request to /campaings.

        Displays all the existing Campaigns already ordered for this Partner
        is as simple as executing a `GET`
        request against the endpoint `/campaigns`

        Args:
            company_id (string): CompanyId to filter the results on
            limit (float, optional): Amount of products returned
            offset (float, optional): Starting point

        Returns:
            ResultSet1Model: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('list_campaigns called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for list_campaigns.')
            _url_path = '/campaings'
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'companyId': company_id,
                'limit': limit,
                'offset': offset
            }
            _query_builder = APIHelper.append_url_with_query_parameters(
                _query_builder,
                _query_parameters
            )
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for list_campaigns.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for list_campaigns.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'list_campaigns')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def retrieve_campaign(self,
                          campaign_id):
        """Does a GET request to /campaigns/{campaignId}.

        Retrieve the details of a specific Campaign. Only Campaigns created by
        the calling Partner can be
        retrieved.

        Args:
            campaign_id (uuid|string): Id of the Campaign that you want to
                retrieve

        Returns:
            ListCampaignResponseModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('retrieve_campaign called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for retrieve_campaign.')
            _url_path = '/campaigns/{campaignId}'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'campaignId': {'value': campaign_id, 'encode': True}
            })
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for retrieve_campaign.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for retrieve_campaign.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'retrieve_campaign')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def check_campaign_status(self,
                              campaign_id):
        """Does a GET request to /campaigns/{campaignId}/status.

        This is a specialized endpoint for Campaign statuses only. Although
        the Campaign Details endpoint also returns the
        status of a campaign, if you only need to get the specific status of a
        Campaign, this endpoint is
        optimized for that.

        Args:
            campaign_id (uuid|string): Id of the Campaign you want the status
                of

        Returns:
            CheckCampaignStatusresponseModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('check_campaign_status called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for check_campaign_status.')
            _url_path = '/campaigns/{campaignId}/status'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'campaignId': {'value': campaign_id, 'encode': True}
            })
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for check_campaign_status.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for check_campaign_status.')
            _request = self.config.http_client.get(_query_url, headers=_headers)
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'check_campaign_status')
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def take_campaign_offline(self,
                              campaign_id,
                              body):
        """Does a PUT request to /campaigns/{campaignId}/cancellation.

        Specific endpoint to take a campaign offline. Keep in mind that
        processing this might
        take some time and it only has an effect if the campaign's status is
        "online".

        Args:
            campaign_id (uuid|string): Id of the Campaign you want to take
                offline
            body (TakeCampaignOfflineRequestModel): TODO: type description
                here.

        Returns:
            TakeCampaignOfflineResponseModel: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('take_campaign_offline called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for take_campaign_offline.')
            _url_path = '/campaigns/{campaignId}/cancellation'
            _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
                'campaignId': {'value': campaign_id, 'encode': True}
            })
            _query_builder = self.config.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for take_campaign_offline.')
            _headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for take_campaign_offline.')
            _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            # Apply authentication scheme on request
            self.apply_auth_schemes(_request, 'token')
    
            _response = self.execute_request(_request, name = 'take_campaign_offline')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for take_campaign_offline.')
            if _response.status_code == 400:
                raise TakeCampaignOfflineErrorResponse2Exception('', _response)
            elif _response.status_code == 404:
                raise TakeCampaignOfflineErrorResponseException('', _response)
            self.validate_response(_response)
    
            decoded = json.loads(_response.text)
    
            return decoded

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
