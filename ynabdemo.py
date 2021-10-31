import json
import ynab_api
from pprint import pprint
from ynab_api.api import accounts_api

with open('secrets.json') as f:
    secrets = json.load(f)
budget_id = secrets['budget_id']
api_key = secrets['api_key']

# Defining the host is optional and defaults to https://api.youneedabudget.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab_api.Configuration(
    host="https://api.youneedabudget.com/v1")

# Configure API key authorization: bearer
configuration.api_key['bearer'] = secrets['api_key']

configuration.api_key_prefix['bearer'] = 'Bearer'

with ynab_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    budget_id = secrets['budget_id']

    try:
        # Create a new account
        api_response = api_instance.get_accounts(budget_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception: %s\n" % e)
