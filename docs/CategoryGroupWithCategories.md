# CategoryGroupWithCategories

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**hidden** | **bool** | Whether or not the category group is hidden | 
**deleted** | **bool** | Whether or not the category group has been deleted.  Deleted category groups will only be included in delta requests. | 
**categories** | [**list[Category]**](Category.md) | Category group categories.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


