# Category

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**category_group_id** | **str** |  | 
**name** | **str** |  | 
**hidden** | **bool** | Whether or not the category is hidden | 
**original_category_group_id** | **str** | If category is hidden this is the id of the category group it originally belonged to before it was hidden. | [optional] 
**note** | **str** |  | [optional] 
**budgeted** | **int** | Budgeted amount in milliunits format | 
**activity** | **int** | Activity amount in milliunits format | 
**balance** | **int** | Balance in milliunits format | 
**goal_type** | **str** | The type of goal, if the category has a goal (TB&#x3D;&#39;Target Category Balance&#39;, TBD&#x3D;&#39;Target Category Balance by Date&#39;, MF&#x3D;&#39;Monthly Funding&#39;, NEED&#x3D;&#39;Plan Your Spending&#39;) | [optional] 
**goal_creation_month** | **date** | The month a goal was created | [optional] 
**goal_target** | **int** | The goal target amount in milliunits | [optional] 
**goal_target_month** | **date** | The target month for the goal to be completed.  Only some goal types specify this date. | [optional] 
**goal_percentage_complete** | **int** | The percentage completion of the goal | [optional] 
**deleted** | **bool** | Whether or not the category has been deleted.  Deleted categories will only be included in delta requests. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


