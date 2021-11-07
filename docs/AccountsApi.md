# ynab_api.AccountsApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](AccountsApi.md#create_account) | **POST** /budgets/{budget_id}/accounts | Create a new account
[**get_account_by_id**](AccountsApi.md#get_account_by_id) | **GET** /budgets/{budget_id}/accounts/{account_id} | Single account
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /budgets/{budget_id}/accounts | Account list


# **create_account**
> AccountResponse create_account(budget_id, data)

Create a new account

Creates a new account

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import accounts_api
from ynab_api.model.account_response import AccountResponse
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.save_account_wrapper import SaveAccountWrapper
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
    api_instance = accounts_api.AccountsApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
    data = SaveAccountWrapper(
        account=SaveAccount(
            name="name_example",
            type="checking",
            balance=1,
        ),
    ) # SaveAccountWrapper | The account to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a new account
        api_response = api_instance.create_account(budget_id, data)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling AccountsApi->create_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) |
 **data** | [**SaveAccountWrapper**](SaveAccountWrapper.md)| The account to create. |

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The account was successfully created |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_id**
> AccountResponse get_account_by_id(budget_id, account_id)

Single account

Returns a single account

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import accounts_api
from ynab_api.model.account_response import AccountResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    account_id = "account_id_example" # str, none_type | The id of the account

    # example passing only required values which don't have defaults set
    try:
        # Single account
        api_response = api_instance.get_account_by_id(budget_id, account_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling AccountsApi->get_account_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **account_id** | **str, none_type**| The id of the account |

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested account |  -  |
**404** | The requested account was not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> AccountsResponse get_accounts(budget_id)

Account list

Returns all accounts

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import accounts_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.accounts_response import AccountsResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    last_knowledge_of_server = 1 # int, none_type | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Account list
        api_response = api_instance.get_accounts(budget_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling AccountsApi->get_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Account list
        api_response = api_instance.get_accounts(budget_id, last_knowledge_of_server=last_knowledge_of_server)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **last_knowledge_of_server** | **int, none_type**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional]

### Return type

[**AccountsResponse**](AccountsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested accounts |  -  |
**404** | No accounts were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

