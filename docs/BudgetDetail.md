# BudgetDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**last_modified_on** | **datetime** | The last time any changes were made to the budget from either a web or mobile client | [optional] 
**first_month** | **date** | The earliest budget month | [optional] 
**last_month** | **date** | The latest budget month | [optional] 
**date_format** | [**DateFormat**](DateFormat.md) |  | [optional] 
**currency_format** | [**CurrencyFormat**](CurrencyFormat.md) |  | [optional] 
**accounts** | [**[Account]**](Account.md) |  | [optional] 
**payees** | [**[Payee]**](Payee.md) |  | [optional] 
**payee_locations** | [**[PayeeLocation]**](PayeeLocation.md) |  | [optional] 
**category_groups** | [**[CategoryGroup]**](CategoryGroup.md) |  | [optional] 
**categories** | [**[Category]**](Category.md) |  | [optional] 
**months** | [**[MonthDetail]**](MonthDetail.md) |  | [optional] 
**transactions** | [**[TransactionSummary]**](TransactionSummary.md) |  | [optional] 
**subtransactions** | [**[SubTransaction]**](SubTransaction.md) |  | [optional] 
**scheduled_transactions** | [**[ScheduledTransactionSummary]**](ScheduledTransactionSummary.md) |  | [optional] 
**scheduled_subtransactions** | [**[ScheduledSubTransaction]**](ScheduledSubTransaction.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


