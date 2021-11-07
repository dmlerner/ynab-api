# SaveSubTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The subtransaction amount in milliunits format. | 
**payee_id** | **str, none_type** | The payee for the subtransaction. | [optional] 
**payee_name** | **str, none_type** | The payee name.  If a &#x60;payee_name&#x60; value is provided and &#x60;payee_id&#x60; has a null value, the &#x60;payee_name&#x60; value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified on parent transaction) or (2) a payee with the same name or (3) creation of a new payee. | [optional] 
**category_id** | **str, none_type** | The category for the subtransaction.  Credit Card Payment categories are not permitted and will be ignored if supplied. | [optional] 
**memo** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


