import json
import ynab_api
from pprint import pprint
from ynab_api.api import accounts_api
'''
secrets.json should be manually generated as:

{
   "budget_id":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
   "api_key":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

To get an api_key:
Sign in to the YNAB web app
and go to the "Account Settings" page
and then to the "Developer Settings" page.
Under the "Personal Access Tokens" section,
click "New Token", enter your password
and click "Generate" to get an access token.

To get your budget_id:
Sign in to the YNAB web app and go the budget of interest.
Copy YOUR_BUDGET_ID from the url:
https://app.youneedabudget.com/YOUR_BUDGET_ID/budget

Or, populate the fields directly in your code.
'''

with open('secrets.json') as f:
    secrets = json.load(f)
budget_id = secrets['budget_id']
api_key = secrets['api_key']

configuration = ynab_api.Configuration(
    host="https://api.youneedabudget.com/v1")
configuration.api_key['bearer'] = api_key
configuration.api_key_prefix['bearer'] = 'Bearer'

with ynab_api.ApiClient(configuration) as api_client:
    api_instance = accounts_api.AccountsApi(api_client)

    try:
        api_response = api_instance.get_accounts(budget_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception: %s\n" % e)
