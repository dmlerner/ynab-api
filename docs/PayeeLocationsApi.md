# ynab_api.PayeeLocationsApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payee_location_by_id**](PayeeLocationsApi.md#get_payee_location_by_id) | **GET** /budgets/{budget_id}/payee_locations/{payee_location_id} | Single payee location
[**get_payee_locations**](PayeeLocationsApi.md#get_payee_locations) | **GET** /budgets/{budget_id}/payee_locations | List payee locations
[**get_payee_locations_by_payee**](PayeeLocationsApi.md#get_payee_locations_by_payee) | **GET** /budgets/{budget_id}/payees/{payee_id}/payee_locations | List locations for a payee


# **get_payee_location_by_id**
> PayeeLocationResponse get_payee_location_by_id(budget_id, payee_location_id)

Single payee location

Returns a single payee location

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import payee_locations_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.payee_location_response import PayeeLocationResponse
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
    api_instance = payee_locations_api.PayeeLocationsApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    payee_location_id = "payee_location_id_example" # str, none_type | id of payee location

    # example passing only required values which don't have defaults set
    try:
        # Single payee location
        api_response = api_instance.get_payee_location_by_id(budget_id, payee_location_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling PayeeLocationsApi->get_payee_location_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **payee_location_id** | **str, none_type**| id of payee location |

### Return type

[**PayeeLocationResponse**](PayeeLocationResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payee location |  -  |
**404** | The payee location was not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payee_locations**
> PayeeLocationsResponse get_payee_locations(budget_id)

List payee locations

Returns all payee locations

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import payee_locations_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.payee_locations_response import PayeeLocationsResponse
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
    api_instance = payee_locations_api.PayeeLocationsApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).

    # example passing only required values which don't have defaults set
    try:
        # List payee locations
        api_response = api_instance.get_payee_locations(budget_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling PayeeLocationsApi->get_payee_locations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |

### Return type

[**PayeeLocationsResponse**](PayeeLocationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of payee locations |  -  |
**404** | No payees locations were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payee_locations_by_payee**
> PayeeLocationsResponse get_payee_locations_by_payee(budget_id, payee_id)

List locations for a payee

Returns all payee locations for a specified payee

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import payee_locations_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.payee_locations_response import PayeeLocationsResponse
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
    api_instance = payee_locations_api.PayeeLocationsApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    payee_id = "payee_id_example" # str, none_type | id of payee

    # example passing only required values which don't have defaults set
    try:
        # List locations for a payee
        api_response = api_instance.get_payee_locations_by_payee(budget_id, payee_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling PayeeLocationsApi->get_payee_locations_by_payee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **payee_id** | **str, none_type**| id of payee |

### Return type

[**PayeeLocationsResponse**](PayeeLocationsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of requested payee locations |  -  |
**404** | No payees locations were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

