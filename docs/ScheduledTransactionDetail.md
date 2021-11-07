# ScheduledTransactionDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** |  | 
**date_first** | **date, none_type** | The first date for which the Scheduled Transaction was scheduled. | 
**date_next** | **date, none_type** | The next date for which the Scheduled Transaction is scheduled. | 
**frequency** | **str, none_type** |  | 
**amount** | **int, none_type** | The scheduled transaction amount in milliunits format | 
**account_id** | **str, none_type** |  | 
**deleted** | **bool** | Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests. | 
**account_name** | **str, none_type** |  | 
**subtransactions** | [**[ScheduledSubTransaction]**](ScheduledSubTransaction.md) | If a split scheduled transaction, the subtransactions. | 
**memo** | **str, none_type** |  | [optional] 
**flag_color** | **str, none_type** | The scheduled transaction flag | [optional] 
**payee_id** | **str, none_type** |  | [optional] 
**category_id** | **str, none_type** |  | [optional] 
**transfer_account_id** | **str, none_type** | If a transfer, the account_id which the scheduled transaction transfers to | [optional] 
**payee_name** | **str, none_type** |  | [optional] 
**category_name** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


