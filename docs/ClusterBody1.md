# ClusterBody1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_password** | **str** | The password for the cluster admin user; will be set to the default password if not provided | [optional] 
**hosts_hostnames** | **list[str]** | A list of hostname to be included in the new cluster | [optional] 
**hosts_ips** | **list[str]** | Management IP addresses; If empty, the hostnames will be resolved; If hosts are highly-available or mixed-networking, use IP set &#x27;&lt;ip&gt;+&lt;ip&gt;+...+&lt;ip&gt;&#x27;; | [optional] 
**join_secrets** | **list[str]** | List of cluster&#x27;s join secrets, used to prevent unauthorized hosts from joining the cluster | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

