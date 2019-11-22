# UpdateTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**account_id** | **str** |  | 
**date** | **date** | The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied it will be ignored. | 
**amount** | **int** | The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a different amount is supplied it will be ignored. | 
**payee_id** | **str** | The payee for the transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as tranfer_payee_id on the account resource. | [optional] 
**payee_name** | **str** | The payee name.  If a payee_name value is provided and payee_id has a null value, the payee_name value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified) or (2) a payee with the same name or (3) creation of a new payee. | [optional] 
**category_id** | **str** | The category for the transaction.  Split and Credit Card Payment categories are not permitted and will be ignored if supplied.  If an existing transaction has a Split category it cannot be changed. | [optional] 
**memo** | **str** |  | [optional] 
**cleared** | **str** | The cleared status of the transaction | [optional] 
**approved** | **bool** | Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default. | [optional] 
**flag_color** | **str** | The transaction flag | [optional] 
**import_id** | **str** | If specified, the new transaction will be assigned this import_id and considered \&quot;imported\&quot;.  We will also attempt to match this imported transaction to an existing \&quot;user-entered\&quot; transation on the same account, with the same amount, and with a date +/-10 days from the imported transaction date.&lt;br&gt;&lt;br&gt;Transactions imported through File Based Import or Direct Import (not through the API) are assigned an import_id in the format: &#39;YNAB:[milliunit_amount]:[iso_date]:[occurrence]&#39;. For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of &#39;YNAB:-294230:2015-12-30:1&#39;.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be &#39;YNAB:-294230:2015-12-30:2&#39;.  Using a consistent format will prevent duplicates through Direct Import and File Based Import.&lt;br&gt;&lt;br&gt;If import_id is omitted or specified as null, the transaction will be treated as a \&quot;user-entered\&quot; transaction. As such, it will be eligible to be matched against transactions later being imported (via DI, FBI, or API). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


