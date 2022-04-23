# ObjectStoresUidBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Access Key ID for AWS Signature authentications | [optional] 
**auth_method** | **str** | Authentication method S3AuthMethod can be None, AWSSignature2 or AWSSignature4 | [optional] 
**bandwidth** | **float** | Bandwidth limitation per core (Mbps) | [optional] 
**hostname** | **str** | Hostname (or IP) of the entrypoint to the object store | [optional] 
**max_blocks_in_data_blob** | **float** | Maximum size to upload to an object store data blob (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB) | [optional] 
**max_concurrent_downloads** | **float** | Maximum number of downloads we concurrently perform on this object store in a single IO node (format - 1..64) | [optional] 
**max_concurrent_removals** | **float** | Maximum number of removals we concurrently perform on this object store in a single IO node (format -  1..64) | [optional] 
**max_concurrent_uploads** | **float** | Maximum number of uploads we concurrently perform on this object store in a single IO node (format - 1..64) | [optional] 
**max_extents_in_data_blob** | **float** | Maximum number of extents data to upload to an object store data blob | [optional] 
**new_name** | **str** | Name of the Object Store | [optional] 
**port** | **float** | Port of the entrypoint to S3 (single Accesser or Load-Balancer) | [optional] 
**protocol** | **str** | One of - HTTP (default), HTTPS, HTTPS_UNVERIFIED | [optional] 
**region** | **str** | Name of the region we are assigned to work with (usually empty) | [optional] 
**secret_key** | **str** | Secret Key for AWS Signature authentications | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

