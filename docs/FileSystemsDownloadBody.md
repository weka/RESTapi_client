# FileSystemsDownloadBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New file system name | 
**group_name** | **str** | Group name | 
**total_capacity** | **float** | Total capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB) | 
**object_storage** | **str** | Object Store name | 
**locator** | **str** | Locator | 
**ssd_capacity** | **float** | SSD capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB) | 
**auth_required** | **bool** | Require the mounting user to be authenticated for mounting this filesystem. This flag is only effective in the root organization, users in non-root organizations must be authenticated to perform a mount operation | [optional] 
**additional_object_storage** | **str** | Additional object Store name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

