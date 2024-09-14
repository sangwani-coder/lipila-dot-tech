# coding: utf-8

"""
    Payments V1

    To facilitate the capability for consumers to make a payment or refund to service providers.

    The version of the OpenAPI document: v1.0
    Contact: developer-support@mtn.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.generate_a_payment_link_for_account_payment_api import GenerateAPaymentLinkForAccountPaymentApi


class TestGenerateAPaymentLinkForAccountPaymentApi(unittest.TestCase):
    """GenerateAPaymentLinkForAccountPaymentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GenerateAPaymentLinkForAccountPaymentApi()

    def tearDown(self) -> None:
        pass

    def test_generate_payment_link(self) -> None:
        """Test case for generate_payment_link

        Provides the ability for a consumer to generate a payment link for account payment
        """
        pass


if __name__ == '__main__':
    unittest.main()
