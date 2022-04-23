# ActiveDirectoryBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain | [optional] 
**enabled** | **bool** |  | [optional] 
**ignore_start_tls_failure** | **bool** | Ignore start TLS failure | [optional] 
**reader_password** | **str** | Reader password | [optional] 
**reader_username** | **str** | Reader username | [optional] 
**role_groups** | **object** | user role can be ClusterAdmin, OrgAdmin, ReadOnly or Regular | [optional] 
**server_timeout_secs** | **float** | LDAP connection timeout in seconds | [optional] 
**server_uri** | **str** | LDAP server URI ([ldap://]hostname[:port] or ldaps://hostname[:port]) | [optional] 
**start_tls** | **bool** | Issue StartTLS after connecting (should not be used with ldaps://) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

