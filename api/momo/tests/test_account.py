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

from openapi_client.models.account import Account

class TestAccount(unittest.TestCase):
    """Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Account:
        """Test Account
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Account`
        """
        model = Account()
        if include_optional:
            return Account(
                id = '',
                name = '',
                description = ''
            )
        else:
            return Account(
        )
        """

    def testAccount(self):
        """Test Account"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()