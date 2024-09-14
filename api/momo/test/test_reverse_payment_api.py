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

from openapi_client.api.reverse_payment_api import ReversePaymentApi


class TestReversePaymentApi(unittest.TestCase):
    """ReversePaymentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReversePaymentApi()

    def tearDown(self) -> None:
        pass

    def test_get_reverse_transaction_history(self) -> None:
        """Test case for get_reverse_transaction_history

        Provides the history or list of revese transactions  to third party.
        """
        pass


if __name__ == '__main__':
    unittest.main()
