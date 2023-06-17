# MonthDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **date** |  | 
**income** | **int** | The total amount of transactions categorized to &#39;Inflow: Ready to Assign&#39; in the month | 
**budgeted** | **int** | The total amount budgeted in the month | 
**activity** | **int** | The total amount of transactions in the month, excluding those categorized to &#39;Inflow: Ready to Assign&#39; | 
**to_be_budgeted** | **int** | The available amount for &#39;Ready to Assign&#39; | 
**deleted** | **bool** | Whether or not the month has been deleted.  Deleted months will only be included in delta requests. | 
**categories** | [**[Category]**](Category.md) | The budget month categories.  Amounts (budgeted, activity, balance, etc.) are specific to the {month} parameter specified. | 
**note** | **str, none_type** |  | [optional] 
**age_of_money** | **int, none_type** | The Age of Money as of the month | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


