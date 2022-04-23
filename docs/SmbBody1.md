# SmbBody1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_domain_mapping_from_id** | **float** | The samba default domain first id | [optional] 
**default_domain_mapping_to_id** | **float** | The samba default domain last id | [optional] 
**domain** | **str** | The domain to join the SMB cluster to | 
**domain_netbios_name** | **str** | The domain netbios name; If not given, the default will be the first part of the given domain name | [optional] 
**encryption** | **str** | Samba cluster encryption | [optional] 
**idmap_backend** | **str** | The samba domain backend type (rid, rfc2307, etc.). Note that rfc2307 requires uid/gid configuration on the Active Directory and is persistent, while rid does not require any Active Directory configuration but in case of range changes | [optional] 
**joined_domain_mapping_from_id** | **float** | The joined domain first id | [optional] 
**joined_domain_mapping_to_id** | **float** | The joined domain last id | [optional] 
**name** | **str** | Domain name | 
**samba_hosts** | **list[str]** | The hosts that will serve via the SMB protocol (pass weka&#x27;s host uid) | [optional] 
**samba_ips** | **list[str]** | IPs used as floating IPs for samba to server SMB in a HA manner. Then should not be assigned to any host on the network (format - A.B.C.D-E.F.G.H or A.B.C.D-F.G.H or A.B.C.D-G.H or A.B.C.D-H) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

