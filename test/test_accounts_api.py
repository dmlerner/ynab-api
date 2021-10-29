"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import ynab_api
from ynab_api.api.accounts_api import AccountsApi  # noqa: E501


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_account(self):
        """Test case for create_account

        Create a new account  # noqa: E501
        """
        pass

    def test_get_account_by_id(self):
        """Test case for get_account_by_id

        Single account  # noqa: E501
        """
        pass

    def test_get_accounts(self):
        """Test case for get_accounts

        Account list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
