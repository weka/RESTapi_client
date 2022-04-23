# swagger_client.HostsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_host**](HostsApi.md#activate_host) | **POST** /hosts/{uid}/activate | Activate host
[**activate_hosts**](HostsApi.md#activate_hosts) | **POST** /hosts/activate | Activate hosts
[**add_host**](HostsApi.md#add_host) | **POST** /hosts | Add host to cluster
[**apply_host**](HostsApi.md#apply_host) | **POST** /hosts/{uid}/apply | Apply host
[**apply_hosts**](HostsApi.md#apply_hosts) | **POST** /hosts/apply | Apply hosts
[**clear_host_failure**](HostsApi.md#clear_host_failure) | **DELETE** /hosts/lastFailureReason/{uid} | Clear host last failure
[**create_host_network**](HostsApi.md#create_host_network) | **POST** /hosts/{uid}/netdevs | Create host network - Need to apply host after
[**deactivate_host**](HostsApi.md#deactivate_host) | **POST** /hosts/{uid}/deactivate | Deactivate host
[**deactivate_hosts**](HostsApi.md#deactivate_hosts) | **POST** /hosts/deactivate | Deactivate hosts
[**get_all_hosts_network**](HostsApi.md#get_all_hosts_network) | **GET** /hosts/netdevs | Get all hosts network
[**get_host_network**](HostsApi.md#get_host_network) | **GET** /hosts/{uid}/netdevs | Get host network
[**get_host_resources**](HostsApi.md#get_host_resources) | **GET** /hosts/{uid}/resources | Get host resources
[**get_hosts**](HostsApi.md#get_hosts) | **GET** /hosts | Get all hosts
[**get_hosts_info**](HostsApi.md#get_hosts_info) | **GET** /hosts/infos | get hosts infos from IPs
[**get_single_host**](HostsApi.md#get_single_host) | **GET** /hosts/{uid} | Get single host
[**remove_host**](HostsApi.md#remove_host) | **DELETE** /hosts/{uid} | Remove host from cluster
[**remove_host_network**](HostsApi.md#remove_host_network) | **DELETE** /hosts/{uid}/netdevs/{netdev_uid} | Remove host network - Need to apply host after
[**update_host**](HostsApi.md#update_host) | **PUT** /hosts/{uid} | Configure host - Need to apply host after

# **activate_host**
> InlineResponse200 activate_host(uid)

Activate host

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Host uid

try:
    # Activate host
    api_response = api_instance.activate_host(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->activate_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Host uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_hosts**
> InlineResponse200 activate_hosts(body)

Activate hosts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostsActivateBody() # HostsActivateBody | 

try:
    # Activate hosts
    api_response = api_instance.activate_hosts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->activate_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostsActivateBody**](HostsActivateBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_host**
> InlineResponse20025 add_host(body)

Add host to cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostsBody() # HostsBody | 

try:
    # Add host to cluster
    api_response = api_instance.add_host(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->add_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostsBody**](HostsBody.md)|  | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_host**
> InlineResponse200 apply_host(uid)

Apply host

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Host uid

try:
    # Apply host
    api_response = api_instance.apply_host(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->apply_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Host uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_hosts**
> InlineResponse200 apply_hosts(body)

Apply hosts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostsApplyBody() # HostsApplyBody | 

try:
    # Apply hosts
    api_response = api_instance.apply_hosts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->apply_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostsApplyBody**](HostsApplyBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_host_failure**
> InlineResponse200 clear_host_failure(uid)

Clear host last failure

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Host uid

try:
    # Clear host last failure
    api_response = api_instance.clear_host_failure(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->clear_host_failure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Host uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_host_network**
> InlineResponse200 create_host_network(body, uid)

Create host network - Need to apply host after

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UidNetdevsBody() # UidNetdevsBody | 
uid = 'uid_example' # str | Host uid

try:
    # Create host network - Need to apply host after
    api_response = api_instance.create_host_network(body, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->create_host_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UidNetdevsBody**](UidNetdevsBody.md)|  | 
 **uid** | **str**| Host uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_host**
> InlineResponse200 deactivate_host(uid)

Deactivate host

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Host uid

try:
    # Deactivate host
    api_response = api_instance.deactivate_host(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->deactivate_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Host uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_hosts**
> InlineResponse200 deactivate_hosts(body)

Deactivate hosts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostsDeactivateBody() # HostsDeactivateBody | 

try:
    # Deactivate hosts
    api_response = api_instance.deactivate_hosts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->deactivate_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostsDeactivateBody**](HostsDeactivateBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_hosts_network**
> InlineResponse20027 get_all_hosts_network()

Get all hosts network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))

try:
    # Get all hosts network
    api_response = api_instance.get_all_hosts_network()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->get_all_hosts_network: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_network**
> InlineResponse20027 get_host_network(uid)

Get host network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Host uid

try:
    # Get host network
    api_response = api_instance.get_host_network(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->get_host_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Host uid | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_resources**
> InlineResponse20028 get_host_resources(uid, type=type)

Get host resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Host uid
type = 'type_example' # str | resource type can be Staging or Stable (Staging if empty) (optional)

try:
    # Get host resources
    api_response = api_instance.get_host_resources(uid, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->get_host_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Host uid | 
 **type** | **str**| resource type can be Staging or Stable (Staging if empty) | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosts**
> InlineResponse20024 get_hosts()

Get all hosts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))

try:
    # Get all hosts
    api_response = api_instance.get_hosts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts: %s\n" % e)
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

# **get_hosts_info**
> InlineResponse20026 get_hosts_info(hostnames_ips=hostnames_ips, info_types=info_types)

get hosts infos from IPs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
hostnames_ips = ['hostnames_ips_example'] # list[str] |  (optional)
info_types = ['info_types_example'] # list[str] |  (optional)

try:
    # get hosts infos from IPs
    api_response = api_instance.get_hosts_info(hostnames_ips=hostnames_ips, info_types=info_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->get_hosts_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostnames_ips** | [**list[str]**](str.md)|  | [optional] 
 **info_types** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_host**
> InlineResponse20025 get_single_host(uid)

Get single host

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Host uid

try:
    # Get single host
    api_response = api_instance.get_single_host(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->get_single_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Host uid | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_host**
> InlineResponse200 remove_host(uid)

Remove host from cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Host uid

try:
    # Remove host from cluster
    api_response = api_instance.remove_host(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->remove_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Host uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_host_network**
> InlineResponse200 remove_host_network(uid, netdev_uid, apply_host=apply_host)

Remove host network - Need to apply host after

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Host uid
netdev_uid = 'netdev_uid_example' # str | network device uid
apply_host = true # bool | Apply the host after this change (optional)

try:
    # Remove host network - Need to apply host after
    api_response = api_instance.remove_host_network(uid, netdev_uid, apply_host=apply_host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->remove_host_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Host uid | 
 **netdev_uid** | **str**| network device uid | 
 **apply_host** | **bool**| Apply the host after this change | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_host**
> InlineResponse200 update_host(body, uid)

Configure host - Need to apply host after

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostsUidBody() # HostsUidBody | 
uid = 'uid_example' # str | Host uid

try:
    # Configure host - Need to apply host after
    api_response = api_instance.update_host(body, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->update_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostsUidBody**](HostsUidBody.md)|  | 
 **uid** | **str**| Host uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

