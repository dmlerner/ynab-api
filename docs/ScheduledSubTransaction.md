# ScheduledSubTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** |  | 
**scheduled_transaction_id** | **str, none_type** |  | 
**amount** | **int** | The scheduled subtransaction amount in milliunits format | 
**deleted** | **bool** | Whether or not the scheduled subtransaction has been deleted.  Deleted scheduled subtransactions will only be included in delta requests. | 
**memo** | **str, none_type** |  | [optional] 
**payee_id** | **str, none_type** |  | [optional] 
**category_id** | **str, none_type** |  | [optional] 
**transfer_account_id** | **str, none_type** | If a transfer, the account_id which the scheduled subtransaction transfers to | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


