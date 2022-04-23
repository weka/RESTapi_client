# SmbSharesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **bool** | Enable Windows ACLs on the share. Will also be translated (as possible) to POSIX ACL | [optional] 
**additional_share_options** | **list[str]** |  | [optional] 
**description** | **str** | A description for samba to show regarding the share | [optional] 
**directory_create_mask** | **str** | POSIX mode mask directories will be created with. E.g. \&quot;0755\&quot; | [optional] 
**encryption** | **str** | Samba share encryption | [optional] 
**file_create_mask** | **str** | POSIX mode mask files will be created with. E.g. \&quot;0744\&quot; | [optional] 
**fs_name** | **str** | Filesystem name to share | 
**mount_options** | **str** | Option to pass to the mount command when mounting weka. NOTE - This parameter is DANGEROUS, use with caution. Incorrect usage may lead to DATA LOSS | [optional] 
**obs_direct** | **bool** | Mount samba in obs-direct mode | [optional] 
**read_only** | **bool** | Mount samba as read-only | [optional] 
**share_name** | **str** | The name of the share being added | 
**sub_path** | **str** | The path inside the filesystem to share | [optional] 
**user_list_type** | **str** |  | [optional] 
**users** | **list[str]** | The list type to which users are added to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

