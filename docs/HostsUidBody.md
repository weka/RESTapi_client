# HostsUidBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_host** | **bool** | Apply the host after this change | [optional] 
**auto_remove_timeout** | **float** | Set how long to wait before removing this host if it disconnects from the cluster (for clients only) | [optional] 
**bandwidth** | **float** | Limit weka&#x27;s bandwidth for the host | [optional] 
**cores** | **float** | Dedicate host&#x27;s cores to weka | [optional] 
**cores_ids_type** | **str** | A core id type | [optional] 
**dedicated** | **bool** | Set the host as dedicated to weka. For example it can be rebooted whenever needed, and configured by weka for optimal performance and stability | [optional] 
**drives_dedicated_cores** | **float** | Drives dedicate cores | [optional] 
**failure_domain** | **str** | Set the host failure domain | [optional] 
**failure_domain_type** | **str** | A failure domain type | [optional] 
**frontend_dedicated_cores** | **float** | Frontend dedicate cores | [optional] 
**management_ips** | **list[str]** | Set the host&#x27;s management node IPs. Setting 2 IPs will turn this hosts networking into highly-available mode | [optional] 
**memory** | **float** | Dedicate a set amount of RAM to weka | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

