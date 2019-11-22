# ynab_api.CategoriesApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_categories**](CategoriesApi.md#get_categories) | **GET** /budgets/{budget_id}/categories | List categories
[**get_category_by_id**](CategoriesApi.md#get_category_by_id) | **GET** /budgets/{budget_id}/categories/{category_id} | Single category
[**get_month_category_by_id**](CategoriesApi.md#get_month_category_by_id) | **GET** /budgets/{budget_id}/months/{month}/categories/{category_id} | Single category for a specific budget month
[**update_month_category**](CategoriesApi.md#update_month_category) | **PATCH** /budgets/{budget_id}/months/{month}/categories/{category_id} | Update a category for a specific month


# **get_categories**
> CategoriesResponse get_categories(budget_id, last_knowledge_of_server=last_knowledge_of_server)

List categories

Returns all categories grouped by category group.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).

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
api_instance = ynab_api.CategoriesApi(ynab_api.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
last_knowledge_of_server = 56 # int | The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. (optional)

try:
    # List categories
    api_response = api_instance.get_categories(budget_id, last_knowledge_of_server=last_knowledge_of_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) | 
 **last_knowledge_of_server** | **int**| The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included. | [optional] 

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
api_instance = ynab_api.CategoriesApi(ynab_api.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
category_id = 'category_id_example' # str | The id of the category

try:
    # Single category
    api_response = api_instance.get_category_by_id(budget_id, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) | 
 **category_id** | **str**| The id of the category | 

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
api_instance = ynab_api.CategoriesApi(ynab_api.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
month = '2013-10-20' # date | The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))
category_id = 'category_id_example' # str | The id of the category

try:
    # Single category for a specific budget month
    api_response = api_instance.get_month_category_by_id(budget_id, month, category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_month_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) | 
 **month** | **date**| The budget month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) | 
 **category_id** | **str**| The id of the category | 

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

Update a category for a specific month

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
api_instance = ynab_api.CategoriesApi(ynab_api.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget)
month = '2013-10-20' # date | The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))
category_id = 'category_id_example' # str | The id of the category
data = ynab_api.SaveMonthCategoryWrapper() # SaveMonthCategoryWrapper | The category to update

try:
    # Update a category for a specific month
    api_response = api_instance.update_month_category(budget_id, month, category_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_month_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**| The id of the budget (\&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) | 
 **month** | **date**| The budget month in ISO format (e.g. 2016-12-01) (\&quot;current\&quot; can also be used to specify the current calendar month (UTC)) | 
 **category_id** | **str**| The id of the category | 
 **data** | [**SaveMonthCategoryWrapper**](SaveMonthCategoryWrapper.md)| The category to update | 

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

