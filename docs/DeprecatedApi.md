# ynab_api.DeprecatedApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_transactions**](DeprecatedApi.md#bulk_create_transactions) | **POST** /budgets/{budget_id}/transactions/bulk | Bulk create transactions


# **bulk_create_transactions**
> BulkResponse bulk_create_transactions(budget_id, transactions)

Bulk create transactions

Creates multiple transactions.  Although this endpoint is still supported, it is recommended to use 'POST /budgets/{budget_id}/transactions' to create multiple transactions.

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import deprecated_api
from ynab_api.model.bulk_response import BulkResponse
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.bulk_transactions import BulkTransactions
from pprint import pprint
# Defining the host is optional and defaults to https://api.youneedabudget.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab_api.Configuration(
    host = "https://api.youneedabudget.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearer
configuration.api_key['bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with ynab_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deprecated_api.DeprecatedApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    transactions = BulkTransactions(
        transactions=[
            SaveTransaction(
                account_id="account_id_example",
                date=dateutil_parser('1970-01-01').date(),
                amount=1,
                payee_id="payee_id_example",
                payee_name="payee_name_example",
                category_id="category_id_example",
                memo="memo_example",
                cleared="cleared",
                approved=True,
                flag_color="red",
                import_id="import_id_example",
                subtransactions=[
                    SaveSubTransaction(
                        amount=1,
                        payee_id="payee_id_example",
                        payee_name="payee_name_example",
                        category_id="category_id_example",
                        memo="memo_example",
                    ),
                ],
            ),
        ],
    ) # BulkTransactions | The list of transactions to create

    # example passing only required values which don't have defaults set
    try:
        # Bulk create transactions
        api_response = api_instance.bulk_create_transactions(budget_id, transactions)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling DeprecatedApi->bulk_create_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **transactions** | [**BulkTransactions**](BulkTransactions.md)| The list of transactions to create |

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The bulk request was processed successfully |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

