# HybridTransactionAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Whether the hybrid transaction represents a regular transaction or a subtransaction | 
**account_name** | **str** |  | 
**parent_transaction_id** | **str** | For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null. | [optional] 
**payee_name** | **str** |  | [optional] 
**category_name** | **str** | The name of the category.  If a split transaction, this will be &#39;Split&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


