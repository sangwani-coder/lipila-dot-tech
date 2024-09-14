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

from openapi_client.models.payment_transaction_status_response_links import PaymentTransactionStatusResponseLinks

class TestPaymentTransactionStatusResponseLinks(unittest.TestCase):
    """PaymentTransactionStatusResponseLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentTransactionStatusResponseLinks:
        """Test PaymentTransactionStatusResponseLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentTransactionStatusResponseLinks`
        """
        model = PaymentTransactionStatusResponseLinks()
        if include_optional:
            return PaymentTransactionStatusResponseLinks(
                var_self = openapi_client.models.payment_transaction_status_response__links_self.PaymentTransactionStatusResponse__Links_Self(
                    href = 'https://host:port/payments/v1/12345', )
            )
        else:
            return PaymentTransactionStatusResponseLinks(
        )
        """

    def testPaymentTransactionStatusResponseLinks(self):
        """Test PaymentTransactionStatusResponseLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
