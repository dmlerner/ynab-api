# ynab_api.PayeesApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payee_by_id**](PayeesApi.md#get_payee_by_id) | **GET** /budgets/{budget_id}/payees/{payee_id} | Single payee
[**get_payees**](PayeesApi.md#get_payees) | **GET** /budgets/{budget_id}/payees | List payees


# **get_payee_by_id**
> PayeeResponse get_payee_by_id(budget_id, payee_id)

Single payee

Returns single payee

### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import ynab_api
from ynab_api.rest import ApiException
from pprint import pprint
configuration = ynab_api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.youneedabudget.com/v1
configuration.host = "https://api.youneedabudget.com/v1"
# Create an instance of the API class
api_instance = ynab_api.PayeesApi(ynab_api.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
payee_id = 'payee_id_example' # str | The id of the payee

try:
    # Single payee
    api_response = api_instance.get_payee_by_id(budget_id, payee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeesApi->get_payee_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) | 
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
> PayeesResponse get_payees(budget_id, last_knowledge_of_server=last_knowledge_of_server)

List payees

Returns all payees

### Example

* Api Key Authentication (bearer):
```python
from __future__ import print_function
import time
import ynab_api
from ynab_api.rest import ApiException
from pprint import pprint
configuration = ynab_api.Configuration()
# Configure API key authorization: bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.youneedabudget.com/v1
configuration.host = "https://api.youneedabudget.com/v1"
# Create an instance of the API class
api_instance = ynab_api.PayeesApi(ynab_api.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. (optional)

try:
    # List payees
    api_response = api_instance.get_payees(budget_id, last_knowledge_of_server=last_knowledge_of_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeesApi->get_payees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) | 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. | [optional] 

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

