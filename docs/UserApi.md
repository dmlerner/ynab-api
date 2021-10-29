# ynab_api.UserApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user**](UserApi.md#get_user) | **GET** /user | User info


# **get_user**
> UserResponse get_user()

User info

Returns authenticated user information

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import user_api
from ynab_api.model.user_response import UserResponse
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # User info
        api_response = api_instance.get_user()
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user info |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

