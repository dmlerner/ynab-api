# SaveTransactionsResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **[str]** | The transaction ids that were saved | 
**server_knowledge** | **int** | The knowledge of the server | 
**transaction** | [**TransactionDetail**](TransactionDetail.md) |  | [optional] 
**transactions** | [**[TransactionDetail]**](TransactionDetail.md) | If multiple transactions were specified, the transactions that were saved | [optional] 
**duplicate_import_ids** | **[str]** | If multiple transactions were specified, a list of import_ids that were not created because of an existing &#x60;import_id&#x60; found on the same account | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


