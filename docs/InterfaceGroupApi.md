# swagger_client.InterfaceGroupApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ip_range_to_interface_group**](InterfaceGroupApi.md#add_ip_range_to_interface_group) | **POST** /interfaceGroups/{uid}/ips | Add ip range to interface group
[**add_port_to_interface_group**](InterfaceGroupApi.md#add_port_to_interface_group) | **POST** /interfaceGroups/{uid}/ports/{host_uid} | Add port to interface group
[**create_interface_group**](InterfaceGroupApi.md#create_interface_group) | **POST** /interfaceGroups | Create interface group
[**delete_interface_group**](InterfaceGroupApi.md#delete_interface_group) | **DELETE** /interfaceGroups/{uid} | delete interface group
[**delete_ip_range_from_interface_group**](InterfaceGroupApi.md#delete_ip_range_from_interface_group) | **DELETE** /interfaceGroups/{uid}/ips/{ips} | Delete ip range from interface group
[**delete_port_from_interface_group**](InterfaceGroupApi.md#delete_port_from_interface_group) | **DELETE** /interfaceGroups/{uid}/ports/{host_uid}/{port} | Delete port from interface group
[**get_interface_group**](InterfaceGroupApi.md#get_interface_group) | **GET** /interfaceGroups/{uid} | Get interface group
[**get_interface_groups**](InterfaceGroupApi.md#get_interface_groups) | **GET** /interfaceGroups | Get interface groups
[**update_interface_group**](InterfaceGroupApi.md#update_interface_group) | **PUT** /interfaceGroups/{uid} | Update interface group

# **add_ip_range_to_interface_group**
> InlineResponse200 add_ip_range_to_interface_group(body, uid)

Add ip range to interface group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterfaceGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.UidIpsBody() # UidIpsBody | 
uid = 'uid_example' # str | Interface group uid

try:
    # Add ip range to interface group
    api_response = api_instance.add_ip_range_to_interface_group(body, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceGroupApi->add_ip_range_to_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UidIpsBody**](UidIpsBody.md)|  | 
 **uid** | **str**| Interface group uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_port_to_interface_group**
> InlineResponse200 add_port_to_interface_group(body, uid, host_uid)

Add port to interface group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterfaceGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.PortsHostUidBody() # PortsHostUidBody | 
uid = 'uid_example' # str | Interface group uid
host_uid = 'host_uid_example' # str | Host uid

try:
    # Add port to interface group
    api_response = api_instance.add_port_to_interface_group(body, uid, host_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceGroupApi->add_port_to_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortsHostUidBody**](PortsHostUidBody.md)|  | 
 **uid** | **str**| Interface group uid | 
 **host_uid** | **str**| Host uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_interface_group**
> InlineResponse20025 create_interface_group(body)

Create interface group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterfaceGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.InterfaceGroupsBody() # InterfaceGroupsBody | 

try:
    # Create interface group
    api_response = api_instance.create_interface_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceGroupApi->create_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterfaceGroupsBody**](InterfaceGroupsBody.md)|  | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_interface_group**
> InlineResponse200 delete_interface_group(uid)

delete interface group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterfaceGroupApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | interface group uid

try:
    # delete interface group
    api_response = api_instance.delete_interface_group(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceGroupApi->delete_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| interface group uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_range_from_interface_group**
> InlineResponse200 delete_ip_range_from_interface_group(uid, ips)

Delete ip range from interface group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterfaceGroupApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | interface group uid
ips = 'ips_example' # str | IP or IP range to delete

try:
    # Delete ip range from interface group
    api_response = api_instance.delete_ip_range_from_interface_group(uid, ips)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceGroupApi->delete_ip_range_from_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| interface group uid | 
 **ips** | **str**| IP or IP range to delete | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_port_from_interface_group**
> InlineResponse200 delete_port_from_interface_group(uid, host_uid, port)

Delete port from interface group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterfaceGroupApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Interface group uid
host_uid = 'host_uid_example' # str | Host uid
port = 'port_example' # str | Port to delete

try:
    # Delete port from interface group
    api_response = api_instance.delete_port_from_interface_group(uid, host_uid, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceGroupApi->delete_port_from_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Interface group uid | 
 **host_uid** | **str**| Host uid | 
 **port** | **str**| Port to delete | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interface_group**
> InlineResponse20025 get_interface_group(uid)

Get interface group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterfaceGroupApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | interface group uid

try:
    # Get interface group
    api_response = api_instance.get_interface_group(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceGroupApi->get_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| interface group uid | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interface_groups**
> InlineResponse20024 get_interface_groups()

Get interface groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterfaceGroupApi(swagger_client.ApiClient(configuration))

try:
    # Get interface groups
    api_response = api_instance.get_interface_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceGroupApi->get_interface_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_interface_group**
> InlineResponse20025 update_interface_group(body, uid)

Update interface group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InterfaceGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.InterfaceGroupsUidBody() # InterfaceGroupsUidBody | 
uid = 'uid_example' # str | interface group uid

try:
    # Update interface group
    api_response = api_instance.update_interface_group(body, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfaceGroupApi->update_interface_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InterfaceGroupsUidBody**](InterfaceGroupsUidBody.md)|  | 
 **uid** | **str**| interface group uid | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

