# LdapBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**server_uri** | **str** | LDAP server URI ([ldap://]hostname[:port] or ldaps://hostname[:port]) | [optional] 
**start_tls** | **bool** | Issue StartTLS after connecting (should not be used with ldaps://) | [optional] 
**ignore_start_tls_failure** | **bool** | Ignore start TLS failure | [optional] 
**server_timeout_secs** | **float** | LDAP connection timeout in seconds | [optional] 
**protocol_version** | **float** | LDAP protocol version | [optional] 
**base_dn** | **str** | Base DN | [optional] 
**user_object_class** | **str** | User object class | [optional] 
**user_id_attribute** | **str** | User ID attribute | [optional] 
**user_revocation_attribute** | **str** | User revocation attribute - If provided, updating this attribute in the LDAP server automatically revokes all user tokens | [optional] 
**group_object_class** | **str** | Group object class | [optional] 
**group_membership_attribute** | **str** | Group membership attribute | [optional] 
**group_id_attribute** | **str** | Group ID attribute | [optional] 
**reader_username** | **str** | Reader username | [optional] 
**reader_password** | **str** | Reader password | [optional] 
**role_groups** | [**LdapRoleGroups**](LdapRoleGroups.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

