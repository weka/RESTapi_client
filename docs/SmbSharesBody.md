# SmbSharesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_name** | **str** | The name of the share being added | 
**fs_name** | **str** | Filesystem name to share | 
**description** | **str** | A description for samba to show regarding the share | [optional] 
**sub_path** | **str** | The path inside the filesystem to share | [optional] 
**mount_options** | **str** | Option to pass to the mount command when mounting weka. NOTE - This parameter is DANGEROUS, use with caution. Incorrect usage may lead to DATA LOSS | [optional] 
**file_create_mask** | **str** | POSIX mode mask files will be created with. E.g. \&quot;0744\&quot; | [optional] 
**directory_create_mask** | **str** | POSIX mode mask directories will be created with. E.g. \&quot;0755\&quot; | [optional] 
**acl** | **bool** | Enable Windows ACLs on the share. Will also be translated (as possible) to POSIX ACL | [optional] 
**obs_direct** | **bool** | Mount samba in obs-direct mode | [optional] 
**encryption** | **str** | Samba share encryption | [optional] 
**read_only** | **bool** | Mount samba as read-only | [optional] 
**user_list_type** | **str** |  | [optional] 
**users** | **list[str]** | The list type to which users are added to | [optional] 
**additional_share_options** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

