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

from openapi_client.models.order_response import OrderResponse

class TestOrderResponse(unittest.TestCase):
    """OrderResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderResponse:
        """Test OrderResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderResponse`
        """
        model = OrderResponse()
        if include_optional:
            return OrderResponse(
                status_code = '0000',
                status_message = '',
                transaction_id = '5345345',
                sequence_no = '12345',
                data = openapi_client.models.data_order.DataOrder(
                    provider_transaction_id = 'FT172145YB21', 
                    order_redirect_url = '', ),
                links = openapi_client.models.order_response__links.OrderResponse__Links(
                    self = openapi_client.models.order_response__links_self.OrderResponse__Links_Self(
                        href = 'https://host:port/payments/payment-link/', ), )
            )
        else:
            return OrderResponse(
        )
        """

    def testOrderResponse(self):
        """Test OrderResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
