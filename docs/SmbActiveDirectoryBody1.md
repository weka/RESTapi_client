# SmbActiveDirectoryBody1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The name of the administrator user to join the domain using it | 
**password** | **str** | The administrator user password | 
**debug_mode** | **bool** | Run the command in debug mode | [optional] 
**server** | **str** | The domain controller server | [optional] 
**create_computer_ou** | **str** | Precreate the computer account in a specific OU | [optional] 
**extra_options** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
**asynchronous** | **bool** |  | [optional] 
**poll** | **bool** |  | [optional] 
**timeout** | **str** | Join command timeout in seconds (format - 3s, 2h, 4m, 1d, 1d5h, 1w, infinite/unlimited) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

