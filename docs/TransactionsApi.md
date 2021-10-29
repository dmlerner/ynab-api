# ynab_api.TransactionsApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction**](TransactionsApi.md#create_transaction) | **POST** /budgets/{budget_id}/transactions | Create a single transaction or multiple transactions
[**get_transaction_by_id**](TransactionsApi.md#get_transaction_by_id) | **GET** /budgets/{budget_id}/transactions/{transaction_id} | Single transaction
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /budgets/{budget_id}/transactions | List transactions
[**get_transactions_by_account**](TransactionsApi.md#get_transactions_by_account) | **GET** /budgets/{budget_id}/accounts/{account_id}/transactions | List account transactions
[**get_transactions_by_category**](TransactionsApi.md#get_transactions_by_category) | **GET** /budgets/{budget_id}/categories/{category_id}/transactions | List category transactions
[**get_transactions_by_payee**](TransactionsApi.md#get_transactions_by_payee) | **GET** /budgets/{budget_id}/payees/{payee_id}/transactions | List payee transactions
[**import_transactions**](TransactionsApi.md#import_transactions) | **POST** /budgets/{budget_id}/transactions/import | Import transactions
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /budgets/{budget_id}/transactions/{transaction_id} | Updates an existing transaction
[**update_transactions**](TransactionsApi.md#update_transactions) | **PATCH** /budgets/{budget_id}/transactions | Update multiple transactions


# **create_transaction**
> SaveTransactionsResponse create_transaction(budget_id, data)

Create a single transaction or multiple transactions

Creates a single transaction or multiple transactions.  If you provide a body containing a `transaction` object, a single transaction will be created and if you provide a body containing a `transactions` array, multiple transactions will be created.  Scheduled transactions cannot be created on this endpoint.

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import transactions_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.save_transactions_response import SaveTransactionsResponse
from ynab_api.model.save_transactions_wrapper import SaveTransactionsWrapper
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
    api_instance = transactions_api.TransactionsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    data = SaveTransactionsWrapper(
        transaction=SaveTransaction(
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
    ) # SaveTransactionsWrapper | The transaction or transactions to create.  To create a single transaction you can specify a value for the `transaction` object and to create multiple transactions you can specify an array of `transactions`.  It is expected that you will only provide a value for one of these objects.

    # example passing only required values which don't have defaults set
    try:
        # Create a single transaction or multiple transactions
        api_response = api_instance.create_transaction(budget_id, data)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **data** | [**SaveTransactionsWrapper**](SaveTransactionsWrapper.md)| The transaction or transactions to create.  To create a single transaction you can specify a value for the &#x60;transaction&#x60; object and to create multiple transactions you can specify an array of &#x60;transactions&#x60;.  It is expected that you will only provide a value for one of these objects. |

### Return type

[**SaveTransactionsResponse**](SaveTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The transaction or transactions were successfully created |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s). |  -  |
**409** | A transaction on the same account with the same &#x60;import_id&#x60; already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id**
> TransactionResponse get_transaction_by_id(budget_id, transaction_id)

Single transaction

Returns a single transaction

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import transactions_api
from ynab_api.model.transaction_response import TransactionResponse
from ynab_api.model.error_response import ErrorResponse
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
    api_instance = transactions_api.TransactionsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    transaction_id = "transaction_id_example" # str | The id of the transaction

    # example passing only required values which don't have defaults set
    try:
        # Single transaction
        api_response = api_instance.get_transaction_by_id(budget_id, transaction_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **transaction_id** | **str**| The id of the transaction |

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transaction |  -  |
**404** | The transaction was not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> TransactionsResponse get_transactions(budget_id)

List transactions

Returns budget transactions

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import transactions_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.transactions_response import TransactionsResponse
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
    api_instance = transactions_api.TransactionsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    since_date = dateutil_parser('1970-01-01').date() # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
    type = "uncategorized" # str | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported. (optional)
    last_knowledge_of_server = 1 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List transactions
        api_response = api_instance.get_transactions(budget_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transactions
        api_response = api_instance.get_transactions(budget_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional]
 **type** | **str**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional]
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional]

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested transactions |  -  |
**400** | An error occurred |  -  |
**404** | No transactions were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_account**
> TransactionsResponse get_transactions_by_account(budget_id, account_id)

List account transactions

Returns all transactions for a specified account

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import transactions_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.transactions_response import TransactionsResponse
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
    api_instance = transactions_api.TransactionsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    account_id = "account_id_example" # str | The id of the account
    since_date = dateutil_parser('1970-01-01').date() # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
    type = "uncategorized" # str | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported. (optional)
    last_knowledge_of_server = 1 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List account transactions
        api_response = api_instance.get_transactions_by_account(budget_id, account_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_by_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List account transactions
        api_response = api_instance.get_transactions_by_account(budget_id, account_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_by_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **account_id** | **str**| The id of the account |
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional]
 **type** | **str**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional]
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional]

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested transactions |  -  |
**404** | No transactions were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_category**
> HybridTransactionsResponse get_transactions_by_category(budget_id, category_id)

List category transactions

Returns all transactions for a specified category

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import transactions_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.hybrid_transactions_response import HybridTransactionsResponse
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
    api_instance = transactions_api.TransactionsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    category_id = "category_id_example" # str | The id of the category
    since_date = dateutil_parser('1970-01-01').date() # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
    type = "uncategorized" # str | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported. (optional)
    last_knowledge_of_server = 1 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List category transactions
        api_response = api_instance.get_transactions_by_category(budget_id, category_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_by_category: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List category transactions
        api_response = api_instance.get_transactions_by_category(budget_id, category_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_by_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **category_id** | **str**| The id of the category |
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional]
 **type** | **str**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional]
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional]

### Return type

[**HybridTransactionsResponse**](HybridTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested transactions |  -  |
**404** | No transactions were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_payee**
> HybridTransactionsResponse get_transactions_by_payee(budget_id, payee_id)

List payee transactions

Returns all transactions for a specified payee

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import transactions_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.hybrid_transactions_response import HybridTransactionsResponse
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
    api_instance = transactions_api.TransactionsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    payee_id = "payee_id_example" # str | The id of the payee
    since_date = dateutil_parser('1970-01-01').date() # date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). (optional)
    type = "uncategorized" # str | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported. (optional)
    last_knowledge_of_server = 1 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List payee transactions
        api_response = api_instance.get_transactions_by_payee(budget_id, payee_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_by_payee: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List payee transactions
        api_response = api_instance.get_transactions_by_payee(budget_id, payee_id, since_date=since_date, type=type, last_knowledge_of_server=last_knowledge_of_server)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions_by_payee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **payee_id** | **str**| The id of the payee |
 **since_date** | **date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional]
 **type** | **str**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional]
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional]

### Return type

[**HybridTransactionsResponse**](HybridTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested transactions |  -  |
**404** | No transactions were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_transactions**
> TransactionsImportResponse import_transactions(budget_id)

Import transactions

Imports available transactions on all linked accounts for the given budget.  Linked accounts allow transactions to be imported directly from a specified financial institution and this endpoint initiates that import.  Sending a request to this endpoint is the equivalent of clicking \"Import\" on each account in the web application or tapping the \"New Transactions\" banner in the mobile applications.  The response for this endpoint contains the transaction ids that have been imported.

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import transactions_api
from ynab_api.model.transactions_import_response import TransactionsImportResponse
from ynab_api.model.error_response import ErrorResponse
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
    api_instance = transactions_api.TransactionsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).

    # example passing only required values which don't have defaults set
    try:
        # Import transactions
        api_response = api_instance.import_transactions(budget_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->import_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |

### Return type

[**TransactionsImportResponse**](TransactionsImportResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful but there were no transactions to import |  -  |
**201** | One or more transactions were imported successfully |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> TransactionResponse update_transaction(budget_id, transaction_id, data)

Updates an existing transaction

Updates a single transaction

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import transactions_api
from ynab_api.model.transaction_response import TransactionResponse
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.save_transaction_wrapper import SaveTransactionWrapper
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
    api_instance = transactions_api.TransactionsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    transaction_id = "transaction_id_example" # str | The id of the transaction
    data = SaveTransactionWrapper(
        transaction=SaveTransaction(
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
    ) # SaveTransactionWrapper | The transaction to update

    # example passing only required values which don't have defaults set
    try:
        # Updates an existing transaction
        api_response = api_instance.update_transaction(budget_id, transaction_id, data)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **transaction_id** | **str**| The id of the transaction |
 **data** | [**SaveTransactionWrapper**](SaveTransactionWrapper.md)| The transaction to update |

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction was successfully updated |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transactions**
> SaveTransactionsResponse update_transactions(budget_id, data)

Update multiple transactions

Updates multiple transactions, by `id` or `import_id`.

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import transactions_api
from ynab_api.model.update_transactions_wrapper import UpdateTransactionsWrapper
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.save_transactions_response import SaveTransactionsResponse
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
    api_instance = transactions_api.TransactionsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    data = UpdateTransactionsWrapper(
        transactions=[
            UpdateTransaction(None),
        ],
    ) # UpdateTransactionsWrapper | The transactions to update. Each transaction must have either an `id` or `import_id` specified. If `id` is specified as null an `import_id` value can be provided which will allow transaction(s) to be updated by their `import_id`. If an `id` is specified, it will always be used for lookup.

    # example passing only required values which don't have defaults set
    try:
        # Update multiple transactions
        api_response = api_instance.update_transactions(budget_id, data)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling TransactionsApi->update_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **data** | [**UpdateTransactionsWrapper**](UpdateTransactionsWrapper.md)| The transactions to update. Each transaction must have either an &#x60;id&#x60; or &#x60;import_id&#x60; specified. If &#x60;id&#x60; is specified as null an &#x60;import_id&#x60; value can be provided which will allow transaction(s) to be updated by their &#x60;import_id&#x60;. If an &#x60;id&#x60; is specified, it will always be used for lookup. |

### Return type

[**SaveTransactionsResponse**](SaveTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**209** | The transactions were successfully updated |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

