# ScheduledTransactionDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**date_first** | **date** | The first date for which the Scheduled Transaction was scheduled. | 
**date_next** | **date** | The next date for which the Scheduled Transaction is scheduled. | 
**frequency** | **str** |  | 
**amount** | **int** | The scheduled transaction amount in milliunits format | 
**account_id** | **str** |  | 
**deleted** | **bool** | Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests. | 
**account_name** | **str** |  | 
**subtransactions** | [**[ScheduledSubTransaction]**](ScheduledSubTransaction.md) | If a split scheduled transaction, the subtransactions. | 
**memo** | **str** |  | [optional] 
**flag_color** | **str** | The scheduled transaction flag | [optional] 
**payee_id** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**transfer_account_id** | **str** | If a transfer, the account_id which the scheduled transaction transfers to | [optional] 
**payee_name** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


