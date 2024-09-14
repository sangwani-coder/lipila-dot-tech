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

from openapi_client.models.order_request import OrderRequest

class TestOrderRequest(unittest.TestCase):
    """OrderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderRequest:
        """Test OrderRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderRequest`
        """
        model = OrderRequest()
        if include_optional:
            return OrderRequest(
                channel = 'Facebook',
                quote_id = '9223372036854775807',
                description = 'Manual Boost for RW',
                authentication_type = 'Query Payment',
                callback_url = '',
                redirect_url = '',
                delivery_method = 'Paylink',
                payer = openapi_client.models.payer.Payer(
                    payer_id_type = 'MSISDN', 
                    payer_id = '233364654737', 
                    payer_note = 'Manual Boost for RWC', 
                    payer_name = '', 
                    payer_email = '', 
                    payer_ref = '233364654737', 
                    payer_surname = 'Orimoloye', 
                    include_payer_charges = False, ),
                paymentmethods = [
                    'Card Payment'
                    ],
                total_amount = openapi_client.models.money_type.MoneyType(
                    amount = 50.0, 
                    units = 'XOF', ),
                item_details = [
                    None
                    ]
            )
        else:
            return OrderRequest(
        )
        """

    def testOrderRequest(self):
        """Test OrderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
