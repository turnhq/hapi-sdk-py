# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from hapi.api_helper import APIHelper


class ContractsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ContractsControllerTests, cls).setUpClass()
        cls.controller = cls.client.contracts
        cls.response_catcher = cls.controller.http_call_back

    # This endpoint exposes a list of channels with support for contracts. For all of the required details for creating a contract or a campaign for each channel, please call the "Retrieve details for channel with support for contracts".
    def test_list_channels(self):
        # Parameters for the API call
        search = None
        limit = None
        offset = None
        accept_language = 'en'

        # Perform the API call through the SDK function
        result = self.controller.list_channels(search, limit, offset, accept_language)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"count":0,"next":"string","previous":"string","results":[{"mc_ena'
            'bled":true,"id":0,"name":"string","url":"string","type":"string"}]'
            '}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))

