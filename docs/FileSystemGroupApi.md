# swagger_client.FileSystemGroupApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_system_group**](FileSystemGroupApi.md#create_file_system_group) | **POST** /fileSystemGroups | Create file system group
[**delete_file_system_group**](FileSystemGroupApi.md#delete_file_system_group) | **DELETE** /fileSystemGroups/{uid} | Delete file system group
[**get_file_system_group**](FileSystemGroupApi.md#get_file_system_group) | **GET** /fileSystemGroups/{uid} | Get file system group
[**get_file_system_groups**](FileSystemGroupApi.md#get_file_system_groups) | **GET** /fileSystemGroups | Get all file system groups
[**update_file_system_group**](FileSystemGroupApi.md#update_file_system_group) | **PUT** /fileSystemGroups/{uid} | Update file system group

# **create_file_system_group**
> InlineResponse20027 create_file_system_group(body)

Create file system group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FileSystemGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.FileSystemGroupsBody() # FileSystemGroupsBody | 

try:
    # Create file system group
    api_response = api_instance.create_file_system_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemGroupApi->create_file_system_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileSystemGroupsBody**](FileSystemGroupsBody.md)|  | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_system_group**
> InlineResponse200 delete_file_system_group(uid)

Delete file system group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FileSystemGroupApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | File system group uid

try:
    # Delete file system group
    api_response = api_instance.delete_file_system_group(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemGroupApi->delete_file_system_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| File system group uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_system_group**
> InlineResponse20027 get_file_system_group(uid)

Get file system group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FileSystemGroupApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | file system group uid

try:
    # Get file system group
    api_response = api_instance.get_file_system_group(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemGroupApi->get_file_system_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| file system group uid | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_system_groups**
> InlineResponse20026 get_file_system_groups()

Get all file system groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FileSystemGroupApi(swagger_client.ApiClient(configuration))

try:
    # Get all file system groups
    api_response = api_instance.get_file_system_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemGroupApi->get_file_system_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_system_group**
> InlineResponse20027 update_file_system_group(body, uid)

Update file system group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FileSystemGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.FileSystemGroupsUidBody() # FileSystemGroupsUidBody | 
uid = 'uid_example' # str | File system group uid

try:
    # Update file system group
    api_response = api_instance.update_file_system_group(body, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemGroupApi->update_file_system_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileSystemGroupsUidBody**](FileSystemGroupsUidBody.md)|  | 
 **uid** | **str**| File system group uid | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

