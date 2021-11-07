import json
import datetime
import ynab_api
from ynab_api.api import categories_api, transactions_api
from ynab_api.model.save_category_response import SaveCategoryResponse
from ynab_api.model.save_month_category_wrapper import SaveMonthCategoryWrapper
from ynab_api.model.save_month_category import SaveMonthCategory
from pprint import pprint
import ynab_api
from pprint import pprint
from ynab_api.api import accounts_api

with open('secrets.json') as f:
    secrets = json.load(f)
budget_id = secrets['budget_id']
api_key = secrets['api_key']

configuration = ynab_api.Configuration(
    host="https://api.youneedabudget.com/v1")
configuration.api_key['bearer'] = api_key
configuration.api_key_prefix['bearer'] = 'Bearer'


def get_accounts():
    with ynab_api.ApiClient(configuration) as api_client:
        api_instance = accounts_api.AccountsApi(api_client)

        try:
            ar = api_response = api_instance.get_accounts(budget_id)
            pprint(api_response)
        except ynab_api.ApiException as e:
            print("Exception: %s\n" % e)


def get_categories():
    with ynab_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = categories_api.CategoriesApi(api_client)
        month = datetime.date.today().isoformat(
        )  # date | The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))
        category_id = "travel"  # str | The id of the category
        data = SaveMonthCategoryWrapper(
            category=SaveMonthCategory(budgeted=1, ),
        )  # SaveMonthCategoryWrapper | The category to update.  Only `budgeted` amount can be updated and any other fields specified will be ignored.

        # example passing only required values which don't have defaults set
        try:
            # Update a category for a specific month
            ar = api_response = api_instance.get_categories(budget_id)
            pprint(api_response)
        except ynab_api.ApiException as e:
            print(
                "Exception when calling CategoriesApi->update_month_category: %s\n"
                % e)


def get_transactions():
    with ynab_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = transactions_api.TransactionsApi(api_client)
        try:
            # Update a category for a specific month
            ar = api_response = api_instance.get_transactions(budget_id)
            pprint(api_response)
        except ynab_api.ApiException as e:
            print(
                "Exception when calling CategoriesApi->update_month_category: %s\n"
                % e)


def update_budget():
    with ynab_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = categories_api.CategoriesApi(api_client)
        month = datetime.date.today().isoformat(
        )  # date | The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))
        #month = "2021-10-07"
        category_id = "93cb7fbb-bd49-4c0b-8580-754f29250dac"
        data = SaveMonthCategoryWrapper(
            category=SaveMonthCategory(budgeted=1, ),
        )  # SaveMonthCategoryWrapper | The category to update.  Only `budgeted` amount can be updated and any other fields specified will be ignored.

        # example passing only required values which don't have defaults set
        try:
            # Update a category for a specific month
            api_response = api_instance.update_month_category(
                budget_id, month, category_id, data)
            pprint(api_response)
        except ynab_api.ApiException as e:
            print(
                "Exception when calling CategoriesApi->update_month_category: %s\n"
                % e)


get_transactions()
get_categories()
get_accounts()
#update_budget()
