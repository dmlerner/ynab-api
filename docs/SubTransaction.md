# SubTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transaction_id** | **str** |  | 
**amount** | **int** | The subtransaction amount in milliunits format | 
**deleted** | **bool** | Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests. | 
**memo** | **str, none_type** |  | [optional] 
**payee_id** | **str, none_type** |  | [optional] 
**payee_name** | **str, none_type** |  | [optional] 
**category_id** | **str, none_type** |  | [optional] 
**category_name** | **str, none_type** |  | [optional] 
**transfer_account_id** | **str, none_type** | If a transfer, the account_id which the subtransaction transfers to | [optional] 
**transfer_transaction_id** | **str, none_type** | If a transfer, the id of transaction on the other side of the transfer | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


