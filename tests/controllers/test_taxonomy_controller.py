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


class TaxonomyControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(TaxonomyControllerTests, cls).setUpClass()
        cls.controller = cls.client.taxonomy
        cls.response_catcher = cls.controller.http_call_back

    # This endpoint returns a tree-like structure of supported Job Functions that can be used to search for Products.
    #Use the `id` key of any Job Function in the response to search for a Product.
    #Each Job Function is associated with [**`Job Titles`**](b3A6MzM0NDA3MzY-job-titles) in a one-to-many fashion.
    #Besides the default English, German and Dutch result translations can be requested by specifying an `Accept-Language: [de|nl]` header.
    def test_retrieve_job_functions_tree(self):
        # Parameters for the API call
        accept_language = 'en'

        # Perform the API call through the SDK function
        result = self.controller.retrieve_job_functions_tree(accept_language)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('[{"id":8,"name":"Education","children":[{"id":5,"name":"Teaching",'
            '"children":[]}]}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))

    # This endpoint returns a list of supported industry names that can be used to search for products. Results are ordered alphabetically.
    #Use the `id` key of any Industry in the response to search for a product.
    #Besides the default English, German and Dutch result translations can be requested by specifying an `Accept-Language: [de|nl]` header.
    def test_list_industries(self):
        # Parameters for the API call
        limit = None
        offset = None
        accept_language = 'en'

        # Perform the API call through the SDK function
        result = self.controller.list_industries(limit, offset, accept_language)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


    # Retrieve all Education Level possible values.
    def test_retrieve_education_levels(self):

        # Perform the API call through the SDK function
        result = self.controller.retrieve_education_levels()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('[{"id":1,"name":[{"languageCode":"nl_NL","value":"Master / Postdoc'
            'toraal"}]}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))

    # Retrieve all Seniority possible values.
    def test_retrieve_seniorities(self):

        # Perform the API call through the SDK function
        result = self.controller.retrieve_seniorities()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('[{"id":3,"name":[{"languageCode":"en_GB","value":"Manager"}]}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))

