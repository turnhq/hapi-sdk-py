# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from hapi.decorators import lazy_property
from hapi.configuration import Configuration
from hapi.configuration import Environment
from hapi.http.auth.token import Token
from hapi.http.auth.customer_id import CustomerId
from hapi.controllers.portfolio_controller import PortfolioController
from hapi.controllers.contracts_controller import ContractsController
from hapi.controllers.campaigns_controller import CampaignsController
from hapi.controllers.taxonomy_controller import TaxonomyController


class HapiClient(object):

    @lazy_property
    def portfolio(self):
        return PortfolioController(self.config, self.auth_managers)

    @lazy_property
    def contracts(self):
        return ContractsController(self.config, self.auth_managers)

    @lazy_property
    def campaigns(self):
        return CampaignsController(self.config, self.auth_managers)

    @lazy_property
    def taxonomy(self):
        return TaxonomyController(self.config, self.auth_managers)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'], environment=Environment.SANDBOX,
                 x_auth_token='TODO: Replace', x_customer_id='TODO: Replace',
                 skip_ssl_cert_verification=False, config=None):
        if config is None:
            self.config = Configuration(
                                         http_client_instance=http_client_instance,
                                         override_http_client_configuration=override_http_client_configuration,
                                         http_call_back=http_call_back,
                                         timeout=timeout,
                                         max_retries=max_retries,
                                         backoff_factor=backoff_factor,
                                         retry_statuses=retry_statuses,
                                         retry_methods=retry_methods,
                                         environment=environment,
                                         x_auth_token=x_auth_token,
                                         x_customer_id=x_customer_id,
                                         skip_ssl_cert_verification=skip_ssl_cert_verification)
        else:
            self.config = config
        self.initialize_auth_managers(self.config)

    def initialize_auth_managers(self, config):
        self.auth_managers = { key: None for key in ['token', 'customerId']}
        self.auth_managers['token'] = Token(config.x_auth_token)
        self.auth_managers['customerId'] = CustomerId(config.x_customer_id)
        return self.auth_managers
