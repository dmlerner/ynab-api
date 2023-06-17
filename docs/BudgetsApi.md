# ynab_api.BudgetsApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_budget_by_id**](BudgetsApi.md#get_budget_by_id) | **GET** /budgets/{budget_id} | Single budget
[**get_budget_settings_by_id**](BudgetsApi.md#get_budget_settings_by_id) | **GET** /budgets/{budget_id}/settings | Budget Settings
[**get_budgets**](BudgetsApi.md#get_budgets) | **GET** /budgets | List budgets


# **get_budget_by_id**
> BudgetDetailResponse get_budget_by_id(budget_id)

Single budget

Returns a single budget with all related entities.  This resource is effectively a full budget export.

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import budgets_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.budget_detail_response import BudgetDetailResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab_api.Configuration(
    host = "https://api.ynab.com/v1"
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
    api_instance = budgets_api.BudgetsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
    last_knowledge_of_server = 1 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Single budget
        api_response = api_instance.get_budget_by_id(budget_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling BudgetsApi->get_budget_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Single budget
        api_response = api_instance.get_budget_by_id(budget_id, last_knowledge_of_server=last_knowledge_of_server)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling BudgetsApi->get_budget_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). |
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional]

### Return type

[**BudgetDetailResponse**](BudgetDetailResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested budget |  -  |
**404** | The specified budget was not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_settings_by_id**
> BudgetSettingsResponse get_budget_settings_by_id(budget_id)

Budget Settings

Returns settings for a budget

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import budgets_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.budget_settings_response import BudgetSettingsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab_api.Configuration(
    host = "https://api.ynab.com/v1"
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
    api_instance = budgets_api.BudgetsApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

    # example passing only required values which don't have defaults set
    try:
        # Budget Settings
        api_response = api_instance.get_budget_settings_by_id(budget_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling BudgetsApi->get_budget_settings_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). |

### Return type

[**BudgetSettingsResponse**](BudgetSettingsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested budget settings |  -  |
**404** | The specified Budget was not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budgets**
> BudgetSummaryResponse get_budgets()

List budgets

Returns budgets list with summary information

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import budgets_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.budget_summary_response import BudgetSummaryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.ynab.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ynab_api.Configuration(
    host = "https://api.ynab.com/v1"
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
    api_instance = budgets_api.BudgetsApi(api_client)
    include_accounts = True # bool | Whether to include the list of budget accounts (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List budgets
        api_response = api_instance.get_budgets(include_accounts=include_accounts)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling BudgetsApi->get_budgets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_accounts** | **bool**| Whether to include the list of budget accounts | [optional]

### Return type

[**BudgetSummaryResponse**](BudgetSummaryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of budgets |  -  |
**404** | No budgets were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

