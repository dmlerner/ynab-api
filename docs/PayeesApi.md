# ynab_api.PayeesApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payee_by_id**](PayeesApi.md#get_payee_by_id) | **GET** /budgets/{budget_id}/payees/{payee_id} | Single payee
[**get_payees**](PayeesApi.md#get_payees) | **GET** /budgets/{budget_id}/payees | List payees


# **get_payee_by_id**
> PayeeResponse get_payee_by_id(budget_id, payee_id)

Single payee

Returns a single payee

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import payees_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.payee_response import PayeeResponse
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
    api_instance = payees_api.PayeesApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
    payee_id = "payee_id_example" # str | The id of the payee

    # example passing only required values which don't have defaults set
    try:
        # Single payee
        api_response = api_instance.get_payee_by_id(budget_id, payee_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling PayeesApi->get_payee_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). |
 **payee_id** | **str**| The id of the payee |

### Return type

[**PayeeResponse**](PayeeResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested payee |  -  |
**404** | The payee was not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payees**
> PayeesResponse get_payees(budget_id)

List payees

Returns all payees

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import payees_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.payees_response import PayeesResponse
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
    api_instance = payees_api.PayeesApi(api_client)
    budget_id = "budget_id_example" # str | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
    last_knowledge_of_server = 1 # int | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List payees
        api_response = api_instance.get_payees(budget_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling PayeesApi->get_payees: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List payees
        api_response = api_instance.get_payees(budget_id, last_knowledge_of_server=last_knowledge_of_server)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling PayeesApi->get_payees: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). |
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional]

### Return type

[**PayeesResponse**](PayeesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested list of payees |  -  |
**404** | No payees were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

