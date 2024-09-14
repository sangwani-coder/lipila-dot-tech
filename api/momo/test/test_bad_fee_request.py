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

from openapi_client.models.bad_fee_request import BadFeeRequest

class TestBadFeeRequest(unittest.TestCase):
    """BadFeeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BadFeeRequest:
        """Test BadFeeRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BadFeeRequest`
        """
        model = BadFeeRequest()
        if include_optional:
            return BadFeeRequest(
                timestamp = '2021-07-21T17:32:28Z',
                status = '400',
                error = 'Bad Request',
                message = '',
                sequence_no = '12345',
                path = '/payments/fee'
            )
        else:
            return BadFeeRequest(
        )
        """

    def testBadFeeRequest(self):
        """Test BadFeeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
