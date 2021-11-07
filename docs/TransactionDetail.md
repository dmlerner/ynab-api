# TransactionDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** |  | 
**date** | **date, none_type** | The transaction date in ISO format (e.g. 2016-12-01) | 
**amount** | **int, none_type** | The transaction amount in milliunits format | 
**cleared** | **str, none_type** | The cleared status of the transaction | 
**approved** | **bool** | Whether or not the transaction is approved | 
**account_id** | **str, none_type** |  | 
**deleted** | **bool** | Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests. | 
**account_name** | **str, none_type** |  | 
**subtransactions** | [**[SubTransaction]**](SubTransaction.md) | If a split transaction, the subtransactions. | 
**memo** | **str, none_type** |  | [optional] 
**flag_color** | **str, none_type** | The transaction flag | [optional] 
**payee_id** | **str, none_type** |  | [optional] 
**category_id** | **str, none_type** |  | [optional] 
**transfer_account_id** | **str, none_type** | If a transfer transaction, the account to which it transfers | [optional] 
**transfer_transaction_id** | **str, none_type** | If a transfer transaction, the id of transaction on the other side of the transfer | [optional] 
**matched_transaction_id** | **str, none_type** | If transaction is matched, the id of the matched transaction | [optional] 
**import_id** | **str, none_type** | If the Transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: &#39;YNAB:[milliunit_amount]:[iso_date]:[occurrence]&#39;.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of &#39;YNAB:-294230:2015-12-30:1&#39;.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be &#39;YNAB:-294230:2015-12-30:2&#39;. | [optional] 
**payee_name** | **str, none_type** |  | [optional] 
**category_name** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


