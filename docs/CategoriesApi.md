# ynab_api.CategoriesApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_categories**](CategoriesApi.md#get_categories) | **GET** /budgets/{budget_id}/categories | List categories
[**get_category_by_id**](CategoriesApi.md#get_category_by_id) | **GET** /budgets/{budget_id}/categories/{category_id} | Single category
[**get_month_category_by_id**](CategoriesApi.md#get_month_category_by_id) | **GET** /budgets/{budget_id}/months/{month}/categories/{category_id} | Single category for a specific budget month
[**update_month_category**](CategoriesApi.md#update_month_category) | **PATCH** /budgets/{budget_id}/months/{month}/categories/{category_id} | Update a category for a specific month


# **get_categories**
> CategoriesResponse get_categories(budget_id)

List categories

Returns all categories grouped by category group.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import categories_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.categories_response import CategoriesResponse
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
    api_instance = categories_api.CategoriesApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    last_knowledge_of_server = 1 # int, none_type | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List categories
        api_response = api_instance.get_categories(budget_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling CategoriesApi->get_categories: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List categories
        api_response = api_instance.get_categories(budget_id, last_knowledge_of_server=last_knowledge_of_server)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **last_knowledge_of_server** | **int, none_type**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional]

### Return type

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The categories grouped by category group |  -  |
**404** | No categories were found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_by_id**
> CategoryResponse get_category_by_id(budget_id, category_id)

Single category

Returns a single category.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import categories_api
from ynab_api.model.category_response import CategoryResponse
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
    api_instance = categories_api.CategoriesApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    category_id = "category_id_example" # str, none_type | The id of the category

    # example passing only required values which don't have defaults set
    try:
        # Single category
        api_response = api_instance.get_category_by_id(budget_id, category_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling CategoriesApi->get_category_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **category_id** | **str, none_type**| The id of the category |

### Return type

[**CategoryResponse**](CategoryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested category |  -  |
**404** | The category not was found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_month_category_by_id**
> CategoryResponse get_month_category_by_id(budget_id, month, category_id)

Single category for a specific budget month

Returns a single category for a specific budget month.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import categories_api
from ynab_api.model.category_response import CategoryResponse
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
    api_instance = categories_api.CategoriesApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    month = dateutil_parser('1970-01-01').date() # date, none_type | The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))
    category_id = "category_id_example" # str, none_type | The id of the category

    # example passing only required values which don't have defaults set
    try:
        # Single category for a specific budget month
        api_response = api_instance.get_month_category_by_id(budget_id, month, category_id)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling CategoriesApi->get_month_category_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **month** | **date, none_type**| The budget month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) |
 **category_id** | **str, none_type**| The id of the category |

### Return type

[**CategoryResponse**](CategoryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested month category |  -  |
**404** | The month category was not was found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_month_category**
> SaveCategoryResponse update_month_category(budget_id, month, category_id, data)

Update a category for a specific month

Update a category for a specific month.  Only `budgeted` amount can be updated.

### Example

* Api Key Authentication (bearer):

```python
import time
import ynab_api
from ynab_api.api import categories_api
from ynab_api.model.error_response import ErrorResponse
from ynab_api.model.save_category_response import SaveCategoryResponse
from ynab_api.model.save_month_category_wrapper import SaveMonthCategoryWrapper
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
    api_instance = categories_api.CategoriesApi(api_client)
    budget_id = "budget_id_example" # str, none_type | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget).
    month = dateutil_parser('1970-01-01').date() # date, none_type | The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))
    category_id = "category_id_example" # str, none_type | The id of the category
    data = SaveMonthCategoryWrapper(
        category=SaveMonthCategory(
            budgeted=1,
        ),
    ) # SaveMonthCategoryWrapper | The category to update.  Only `budgeted` amount can be updated and any other fields specified will be ignored.

    # example passing only required values which don't have defaults set
    try:
        # Update a category for a specific month
        api_response = api_instance.update_month_category(budget_id, month, category_id, data)
        pprint(api_response)
    except ynab_api.ApiException as e:
        print("Exception when calling CategoriesApi->update_month_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str, none_type**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget). |
 **month** | **date, none_type**| The budget month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) |
 **category_id** | **str, none_type**| The id of the category |
 **data** | [**SaveMonthCategoryWrapper**](SaveMonthCategoryWrapper.md)| The category to update.  Only &#x60;budgeted&#x60; amount can be updated and any other fields specified will be ignored. |

### Return type

[**SaveCategoryResponse**](SaveCategoryResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The month category was successfully updated |  -  |
**400** | The request could not be understood due to malformed syntax or validation error(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

