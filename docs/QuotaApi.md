# swagger_client.QuotaApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_quota**](QuotaApi.md#delete_quota) | **DELETE** /fileSystems/{uid}/quota/{inode_context} | Remove the quota from a directory
[**get_quota**](QuotaApi.md#get_quota) | **GET** /fileSystems/{uid}/quota/{inode_context} | Get the parameters of a specific directory quota
[**get_quota_deprecated**](QuotaApi.md#get_quota_deprecated) | **GET** /quota | Get file system quota
[**list_quotas**](QuotaApi.md#list_quotas) | **GET** /fileSystems/{uid}/quota/ | Get a list of quotas in the file system
[**patch_quota**](QuotaApi.md#patch_quota) | **PATCH** /fileSystems/{uid}/quota/{inode_context} | Patch the parameters of a directory quota
[**put_quota**](QuotaApi.md#put_quota) | **PUT** /fileSystems/{uid}/quota/{inode_context} | Set a quota on a directory

# **delete_quota**
> InlineResponse20023 delete_quota(uid, inode_context, path=path)

Remove the quota from a directory

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.QuotaApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | file system uid
inode_context = 'inode_context_example' # str | directory's inode id
path = 'path_example' # str |  (optional)

try:
    # Remove the quota from a directory
    api_response = api_instance.delete_quota(uid, inode_context, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->delete_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| file system uid | 
 **inode_context** | **str**| directory&#x27;s inode id | 
 **path** | **str**|  | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quota**
> InlineResponse20021 get_quota(uid, inode_context)

Get the parameters of a specific directory quota

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.QuotaApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | file system uid
inode_context = 'inode_context_example' # str | directory's inode id

try:
    # Get the parameters of a specific directory quota
    api_response = api_instance.get_quota(uid, inode_context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->get_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| file system uid | 
 **inode_context** | **str**| directory&#x27;s inode id | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quota_deprecated**
> InlineResponse20054 get_quota_deprecated(type, uid, next_token=next_token)

Get file system quota

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.QuotaApi(wekarestapi.ApiClient(configuration))
type = 'type_example' # str | Quota type
uid = 'uid_example' # str | File system uid
next_token = 'next_token_example' # str | Token to get the next page (optional)

try:
    # Get file system quota
    api_response = api_instance.get_quota_deprecated(type, uid, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->get_quota_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Quota type | 
 **uid** | **str**| File system uid | 
 **next_token** | **str**| Token to get the next page | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quotas**
> InlineResponse20020 list_quotas(uid, next_token=next_token)

Get a list of quotas in the file system

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.QuotaApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | file system uid
next_token = 'next_token_example' # str | Token to get the next page (optional)

try:
    # Get a list of quotas in the file system
    api_response = api_instance.list_quotas(uid, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->list_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| file system uid | 
 **next_token** | **str**| Token to get the next page | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_quota**
> InlineResponse20021 patch_quota(uid, inode_context, path=path, hard_limit_bytes=hard_limit_bytes, soft_limit_bytes=soft_limit_bytes, grace_seconds=grace_seconds, owner=owner)

Patch the parameters of a directory quota

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.QuotaApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | file system uid
inode_context = 'inode_context_example' # str | directory's inode id
path = 'path_example' # str |  (optional)
hard_limit_bytes = 1.2 # float | 0 for unlimited (optional)
soft_limit_bytes = 1.2 # float | 0 for unlimited (optional)
grace_seconds = 1.2 # float |  (optional)
owner = 'owner_example' # str |  (optional)

try:
    # Patch the parameters of a directory quota
    api_response = api_instance.patch_quota(uid, inode_context, path=path, hard_limit_bytes=hard_limit_bytes, soft_limit_bytes=soft_limit_bytes, grace_seconds=grace_seconds, owner=owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->patch_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| file system uid | 
 **inode_context** | **str**| directory&#x27;s inode id | 
 **path** | **str**|  | [optional] 
 **hard_limit_bytes** | **float**| 0 for unlimited | [optional] 
 **soft_limit_bytes** | **float**| 0 for unlimited | [optional] 
 **grace_seconds** | **float**|  | [optional] 
 **owner** | **str**|  | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_quota**
> InlineResponse20022 put_quota(uid, inode_context, hard_limit_bytes, soft_limit_bytes, grace_seconds, path=path, owner=owner)

Set a quota on a directory

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.QuotaApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | file system uid
inode_context = 'inode_context_example' # str | directory's inode id
hard_limit_bytes = 1.2 # float | 0 for unlimited
soft_limit_bytes = 1.2 # float | 0 for unlimited
grace_seconds = 1.2 # float | 
path = 'path_example' # str |  (optional)
owner = 'owner_example' # str |  (optional)

try:
    # Set a quota on a directory
    api_response = api_instance.put_quota(uid, inode_context, hard_limit_bytes, soft_limit_bytes, grace_seconds, path=path, owner=owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->put_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| file system uid | 
 **inode_context** | **str**| directory&#x27;s inode id | 
 **hard_limit_bytes** | **float**| 0 for unlimited | 
 **soft_limit_bytes** | **float**| 0 for unlimited | 
 **grace_seconds** | **float**|  | 
 **path** | **str**|  | [optional] 
 **owner** | **str**|  | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

