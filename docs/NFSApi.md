# swagger_client.NFSApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client_group_rule**](NFSApi.md#add_client_group_rule) | **POST** /nfs/clientGroups/{uid}/rules | create rule for nfs client group
[**add_nfs_permission**](NFSApi.md#add_nfs_permission) | **POST** /nfs/permissions | Add NFS permission
[**create_client_group**](NFSApi.md#create_client_group) | **POST** /nfs/clientGroups | Create nfs client group
[**delete_client_group**](NFSApi.md#delete_client_group) | **DELETE** /nfs/clientGroups/{uid} | Delete nfs client group
[**delete_client_group_rule**](NFSApi.md#delete_client_group_rule) | **DELETE** /nfs/clientGroups/{uid}/rules/{rule_uid} | Delete rule for nfs client group
[**delete_nfs_permission**](NFSApi.md#delete_nfs_permission) | **DELETE** /nfs/permissions/{uid} | Remove NFS permission
[**get_client_group**](NFSApi.md#get_client_group) | **GET** /nfs/clientGroups/{uid} | Get nfs client group
[**get_client_groups**](NFSApi.md#get_client_groups) | **GET** /nfs/clientGroups | Get all nfs client groups
[**get_nfs_global_config**](NFSApi.md#get_nfs_global_config) | **GET** /nfs/globalConfig | Get NFS global configuration
[**get_nfs_permission**](NFSApi.md#get_nfs_permission) | **GET** /nfs/permissions/{uid} | Get NFS permission
[**get_nfs_permissions**](NFSApi.md#get_nfs_permissions) | **GET** /nfs/permissions | Get NFS permissions
[**update_nfs_global_config**](NFSApi.md#update_nfs_global_config) | **PUT** /nfs/globalConfig | Update NFS global configuration
[**update_nfs_permission**](NFSApi.md#update_nfs_permission) | **PUT** /nfs/permissions/{uid} | Update NFS permission

# **add_client_group_rule**
> InlineResponse200 add_client_group_rule(body, uid)

create rule for nfs client group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
body = swagger_client.UidRulesBody() # UidRulesBody | 
uid = 'uid_example' # str | group uid

try:
    # create rule for nfs client group
    api_response = api_instance.add_client_group_rule(body, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->add_client_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UidRulesBody**](UidRulesBody.md)|  | 
 **uid** | **str**| group uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_nfs_permission**
> InlineResponse20046 add_nfs_permission(body=body)

Add NFS permission

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
body = swagger_client.NfsPermissionsBody() # NfsPermissionsBody |  (optional)

try:
    # Add NFS permission
    api_response = api_instance.add_nfs_permission(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->add_nfs_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NfsPermissionsBody**](NfsPermissionsBody.md)|  | [optional] 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_group**
> InlineResponse20042 create_client_group(body)

Create nfs client group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
body = swagger_client.NfsClientGroupsBody() # NfsClientGroupsBody | 

try:
    # Create nfs client group
    api_response = api_instance.create_client_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->create_client_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NfsClientGroupsBody**](NfsClientGroupsBody.md)|  | 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_group**
> InlineResponse200 delete_client_group(uid)

Delete nfs client group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | group uid

try:
    # Delete nfs client group
    api_response = api_instance.delete_client_group(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->delete_client_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| group uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_group_rule**
> InlineResponse200 delete_client_group_rule(uid, rule_uid)

Delete rule for nfs client group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | group uid
rule_uid = 'rule_uid_example' # str | 

try:
    # Delete rule for nfs client group
    api_response = api_instance.delete_client_group_rule(uid, rule_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->delete_client_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| group uid | 
 **rule_uid** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nfs_permission**
> InlineResponse200 delete_nfs_permission(uid, path=path)

Remove NFS permission

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Permission uid
path = 'path_example' # str | Default \"/\" (optional)

try:
    # Remove NFS permission
    api_response = api_instance.delete_nfs_permission(uid, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->delete_nfs_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Permission uid | 
 **path** | **str**| Default \&quot;/\&quot; | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_group**
> InlineResponse20043 get_client_group(uid)

Get nfs client group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | group uid

try:
    # Get nfs client group
    api_response = api_instance.get_client_group(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->get_client_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| group uid | 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_groups**
> InlineResponse20041 get_client_groups()

Get all nfs client groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))

try:
    # Get all nfs client groups
    api_response = api_instance.get_client_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->get_client_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_global_config**
> InlineResponse20044 get_nfs_global_config()

Get NFS global configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))

try:
    # Get NFS global configuration
    api_response = api_instance.get_nfs_global_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->get_nfs_global_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_permission**
> InlineResponse20046 get_nfs_permission(uid)

Get NFS permission

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Permission uid

try:
    # Get NFS permission
    api_response = api_instance.get_nfs_permission(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->get_nfs_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Permission uid | 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_permissions**
> InlineResponse20045 get_nfs_permissions(fs_uid=fs_uid)

Get NFS permissions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
fs_uid = 'fs_uid_example' # str | File system uid (optional)

try:
    # Get NFS permissions
    api_response = api_instance.get_nfs_permissions(fs_uid=fs_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->get_nfs_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_uid** | **str**| File system uid | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_global_config**
> InlineResponse200 update_nfs_global_config(body)

Update NFS global configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
body = swagger_client.NfsGlobalConfigBody() # NfsGlobalConfigBody | 

try:
    # Update NFS global configuration
    api_response = api_instance.update_nfs_global_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->update_nfs_global_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NfsGlobalConfigBody**](NfsGlobalConfigBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_permission**
> InlineResponse200 update_nfs_permission(uid, body=body)

Update NFS permission

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.NFSApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | Permission uid
body = swagger_client.PermissionsUidBody() # PermissionsUidBody |  (optional)

try:
    # Update NFS permission
    api_response = api_instance.update_nfs_permission(uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFSApi->update_nfs_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Permission uid | 
 **body** | [**PermissionsUidBody**](PermissionsUidBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

