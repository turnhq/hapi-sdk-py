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


class PortfolioControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(PortfolioControllerTests, cls).setUpClass()
        cls.controller = cls.client.portfolio
        cls.response_catcher = cls.controller.http_call_back

    # For a detailed tutorial on how to get started with portfolio search v2, check out our [Quickstart Tutorial](https://pkb.stoplight.io/docs/search/docs/Tutorial.md).
    #For an implementation demo of the product search experience, check out our [Developer Portal](http://vonq.io/pkb).
    #This endpoint exposes a list of Products with the options to search by Location, Job Title, Job Function and Industry.
    #Products are ranked by their relevancy to the search terms.
    #Optionally, products can filtered by Location.
    #Values for each parameter can be fetched by calling the other endpoints in this section.
    #Calling this endpoint will guarantee that the Products you see are configured for you as our Partner.
    #Besides the default English, German and Dutch result translations can be requested by specifying an `Accept-Language: [de|nl]` header.
    def test_search_products(self):
        # Parameters for the API call
        limit = None
        offset = None
        include_location_id = None
        exact_location_id = None
        job_function_id = None
        job_title_id = None
        industry_id = None
        duration_from = None
        duration_to = None
        name = None
        currency = None
        sort_by = 'relevant'
        recommended = None
        mc_enabled = None
        accept_language = 'en'
        exclude_recommended = False

        # Perform the API call through the SDK function
        result = self.controller.search_products(limit, offset, include_location_id, exact_location_id, job_function_id, job_title_id, industry_id, duration_from, duration_to, name, currency, sort_by, recommended, mc_enabled, accept_language, exclude_recommended)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


