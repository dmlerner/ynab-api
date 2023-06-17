# Category


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**category_group_id** | **str** |  | 
**name** | **str** |  | 
**hidden** | **bool** | Whether or not the category is hidden | 
**budgeted** | **int** | Budgeted amount in milliunits format | 
**activity** | **int** | Activity amount in milliunits format | 
**balance** | **int** | Balance in milliunits format | 
**deleted** | **bool** | Whether or not the category has been deleted.  Deleted categories will only be included in delta requests. | 
**category_group_name** | **str, none_type** |  | [optional] 
**original_category_group_id** | **str, none_type** | DEPRECATED: No longer used.  Value will always be null. | [optional] 
**note** | **str, none_type** |  | [optional] 
**goal_type** | **str, none_type** | The type of goal, if the category has a goal (TB&#x3D;&#39;Target Category Balance&#39;, TBD&#x3D;&#39;Target Category Balance by Date&#39;, MF&#x3D;&#39;Monthly Funding&#39;, NEED&#x3D;&#39;Plan Your Spending&#39;) | [optional] 
**goal_day** | **int, none_type** | A day offset modifier for the goal&#39;s due date. When goal_cadence is 2 (Weekly), this value specifies which day of the week the goal is due (0 &#x3D; Sunday, 6 &#x3D; Saturday). Otherwise, this value specifies which day of the month the goal is due (1 &#x3D; 1st, 31 &#x3D; 31st, null &#x3D; Last day of Month). | [optional] 
**goal_cadence** | **int, none_type** | The goal cadence. Value in range 0-14. There are two subsets of these values which behave differently. For values 0, 1, 2, and 13, the goal&#39;s due date repeats every goal_cadence * goal_cadence_frequency, where 0 &#x3D; None, 1 &#x3D; Monthly, 2 &#x3D; Weekly, and 13 &#x3D; Yearly. For example, goal_cadence 1 with goal_cadence_frequency 2 means the goal is due every other month. For values 3-12 and 14, goal_cadence_frequency is ignored and the goal&#39;s due date repeats every goal_cadence, where 3 &#x3D; Every 2 Months, 4 &#x3D; Every 3 Months, ..., 12 &#x3D; Every 11 Months, and 14 &#x3D; Every 2 Years. | [optional] 
**goal_cadence_frequency** | **int, none_type** | The goal cadence frequency. When goal_cadence is 0, 1, 2, or 13, a goal&#39;s due date repeats every goal_cadence * goal_cadence_frequency. For example, goal_cadence 1 with goal_cadence_frequency 2 means the goal is due every other month.  When goal_cadence is 3-12 or 14, goal_cadence_frequency is ignored. | [optional] 
**goal_creation_month** | **date, none_type** | The month a goal was created | [optional] 
**goal_target** | **int, none_type** | The goal target amount in milliunits | [optional] 
**goal_target_month** | **date, none_type** | The original target month for the goal to be completed.  Only some goal types specify this date. | [optional] 
**goal_percentage_complete** | **int, none_type** | The percentage completion of the goal | [optional] 
**goal_months_to_budget** | **int, none_type** | The number of months, including the current month, left in the current goal period. | [optional] 
**goal_under_funded** | **int, none_type** | The amount of funding still needed in the current month to stay on track towards completing the goal within the current goal period.  This amount will generally correspond to the &#39;Underfunded&#39; amount in the web and mobile clients except when viewing a category with a Needed for Spending Goal in a future month.  The web and mobile clients will ignore any funding from a prior goal period when viewing category with a Needed for Spending Goal in a future month. | [optional] 
**goal_overall_funded** | **int, none_type** | The total amount funded towards the goal within the current goal period. | [optional] 
**goal_overall_left** | **int, none_type** | The amount of funding still needed to complete the goal within the current goal period. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


