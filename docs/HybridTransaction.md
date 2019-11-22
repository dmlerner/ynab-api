# HybridTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**date** | **date** | The transaction date in ISO format (e.g. 2016-12-01) | 
**amount** | **int** | The transaction amount in milliunits format | 
**memo** | **str** |  | [optional] 
**cleared** | **str** | The cleared status of the transaction | 
**approved** | **bool** | Whether or not the transaction is approved | 
**flag_color** | **str** | The transaction flag | [optional] 
**account_id** | **str** |  | 
**payee_id** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**transfer_account_id** | **str** | If a transfer transaction, the account to which it transfers | [optional] 
**transfer_transaction_id** | **str** | If a transfer transaction, the id of transaction on the other side of the transfer | [optional] 
**matched_transaction_id** | **str** | If transaction is matched, the id of the matched transaction | [optional] 
**import_id** | **str** | If the Transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: &#39;YNAB:[milliunit_amount]:[iso_date]:[occurrence]&#39;.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of &#39;YNAB:-294230:2015-12-30:1&#39;.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be &#39;YNAB:-294230:2015-12-30:2&#39;. | [optional] 
**deleted** | **bool** | Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests. | 
**type** | **str** | Whether the hybrid transaction represents a regular transaction or a subtransaction | 
**parent_transaction_id** | **str** | For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null. | [optional] 
**account_name** | **str** |  | 
**payee_name** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


