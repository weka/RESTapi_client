# UidNetdevsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | Network device pci-slot/mac-address/interface-name(s) | [optional] 
**ips_type** | **str** | POOL - IPs from the default data networking IP pool would be used, USER - configured by the user | [optional] 
**ips** | **list[str]** | IPs to be allocated to cores using the device. If not given - IPs may be set automatically according the interface&#x27;s IPs, or taken from the default networking IPs pool (format - A.B.C.D-E.F.G.H or A.B.C.D-F.G.H or A.B.C.D-G.H or A.B.C.D-H) | [optional] 
**gateway** | **str** | Default gateway IP. In AWS this value is auto-detected, otherwise the default data networking gateway will be used | [optional] 
**netmask** | **float** | Netmask in bits number. In AWS this value is auto-detected, otherwise the default data networking netmask will be used | [optional] 
**name** | **str** | If empty, a name will be auto generated | [optional] 
**apply_host** | **bool** | Apply the host after this change | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

