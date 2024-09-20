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

from openapi_client.models.data_order import DataOrder

class TestDataOrder(unittest.TestCase):
    """DataOrder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataOrder:
        """Test DataOrder
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataOrder`
        """
        model = DataOrder()
        if include_optional:
            return DataOrder(
                provider_transaction_id = 'FT172145YB21',
                order_redirect_url = ''
            )
        else:
            return DataOrder(
        )
        """

    def testDataOrder(self):
        """Test DataOrder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()