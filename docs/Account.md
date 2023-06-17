# Account


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | [**AccountType**](AccountType.md) |  | 
**on_budget** | **bool** | Whether this account is on budget or not | 
**closed** | **bool** | Whether this account is closed or not | 
**balance** | **int** | The current balance of the account in milliunits format | 
**cleared_balance** | **int** | The current cleared balance of the account in milliunits format | 
**uncleared_balance** | **int** | The current uncleared balance of the account in milliunits format | 
**transfer_payee_id** | **str** | The payee id which should be used when transferring to this account | 
**deleted** | **bool** | Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests. | 
**note** | **str, none_type** |  | [optional] 
**direct_import_linked** | **bool** | Whether or not the account is linked to a financial institution for automatic transaction import. | [optional] 
**direct_import_in_error** | **bool** | If an account linked to a financial institution (direct_import_linked&#x3D;true) and the linked connection is not in a healthy state, this will be true. | [optional] 
**last_reconciled_at** | **datetime, none_type** | A date/time specifying when the account was last reconciled. | [optional] 
**debt_original_balance** | **int, none_type** | The original debt/loan account balance, specified in milliunits format. | [optional] 
**debt_interest_rates** | [**LoanAccountPeriodicValue**](LoanAccountPeriodicValue.md) |  | [optional] 
**debt_minimum_payments** | [**LoanAccountPeriodicValue**](LoanAccountPeriodicValue.md) |  | [optional] 
**debt_escrow_amounts** | [**LoanAccountPeriodicValue**](LoanAccountPeriodicValue.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


