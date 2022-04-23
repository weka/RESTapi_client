# LdapBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_dn** | **str** | Base DN | [optional] 
**enabled** | **bool** |  | [optional] 
**group_id_attribute** | **str** | Group ID attribute | [optional] 
**group_membership_attribute** | **str** | Group membership attribute | [optional] 
**group_object_class** | **str** | Group object class | [optional] 
**ignore_start_tls_failure** | **bool** | Ignore start TLS failure | [optional] 
**protocol_version** | **float** | LDAP protocol version | [optional] 
**reader_password** | **str** | Reader password | [optional] 
**reader_username** | **str** | Reader username | [optional] 
**role_groups** | [**LdapRoleGroups**](LdapRoleGroups.md) |  | [optional] 
**server_timeout_secs** | **float** | LDAP connection timeout in seconds | [optional] 
**server_uri** | **str** | LDAP server URI ([ldap://]hostname[:port] or ldaps://hostname[:port]) | [optional] 
**start_tls** | **bool** | Issue StartTLS after connecting (should not be used with ldaps://) | [optional] 
**user_id_attribute** | **str** | User ID attribute | [optional] 
**user_object_class** | **str** | User object class | [optional] 
**user_revocation_attribute** | **str** | User revocation attribute - If provided, updating this attribute in the LDAP server automatically revokes all user tokens | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

