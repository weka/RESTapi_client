# swagger_client.SnapshotsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_snapshot**](SnapshotsApi.md#copy_snapshot) | **POST** /snapshots/{uid}/copy | Copy snapshot from the same file system
[**create_snapshot**](SnapshotsApi.md#create_snapshot) | **POST** /snapshots | Create snapshot
[**delete_snapshot**](SnapshotsApi.md#delete_snapshot) | **DELETE** /snapshots/{uid} | Delete snapshot
[**get_snapshot**](SnapshotsApi.md#get_snapshot) | **GET** /snapshots/{uid} | Get snapshot
[**get_snapshots**](SnapshotsApi.md#get_snapshots) | **GET** /snapshots | Get snapshots
[**restore_file_system_from_snapshot**](SnapshotsApi.md#restore_file_system_from_snapshot) | **POST** /snapshots/{fs_uid}/{uid}/restore | Restore file system from snapshot
[**update_snapshot**](SnapshotsApi.md#update_snapshot) | **PUT** /snapshots/{uid} | Update snapshot
[**upload_snapshot**](SnapshotsApi.md#upload_snapshot) | **POST** /snapshots/{uid}/upload | Upload snapshot to object store

# **copy_snapshot**
> InlineResponse20072 copy_snapshot(uid, body=body)

Copy snapshot from the same file system

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.SnapshotsApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | Snapshot uid
body = wekarestapi.UidCopyBody() # UidCopyBody |  (optional)

try:
    # Copy snapshot from the same file system
    api_response = api_instance.copy_snapshot(uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->copy_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Snapshot uid | 
 **body** | [**UidCopyBody**](UidCopyBody.md)|  | [optional] 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot**
> InlineResponse20072 create_snapshot(body=body)

Create snapshot

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.SnapshotsApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.SnapshotsBody() # SnapshotsBody |  (optional)

try:
    # Create snapshot
    api_response = api_instance.create_snapshot(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->create_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnapshotsBody**](SnapshotsBody.md)|  | [optional] 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot**
> InlineResponse200 delete_snapshot(uid)

Delete snapshot

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.SnapshotsApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | Snapshot uid

try:
    # Delete snapshot
    api_response = api_instance.delete_snapshot(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->delete_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Snapshot uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot**
> InlineResponse20072 get_snapshot(uid)

Get snapshot

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.SnapshotsApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | Snapshot uid

try:
    # Get snapshot
    api_response = api_instance.get_snapshot(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Snapshot uid | 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshots**
> InlineResponse20071 get_snapshots()

Get snapshots

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.SnapshotsApi(wekarestapi.ApiClient(configuration))

try:
    # Get snapshots
    api_response = api_instance.get_snapshots()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_snapshots: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_file_system_from_snapshot**
> InlineResponse20072 restore_file_system_from_snapshot(fs_uid, uid)

Restore file system from snapshot

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.SnapshotsApi(wekarestapi.ApiClient(configuration))
fs_uid = 'fs_uid_example' # str | 
uid = 'uid_example' # str | snapshot uid

try:
    # Restore file system from snapshot
    api_response = api_instance.restore_file_system_from_snapshot(fs_uid, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->restore_file_system_from_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fs_uid** | **str**|  | 
 **uid** | **str**| snapshot uid | 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot**
> InlineResponse20072 update_snapshot(uid, body=body)

Update snapshot

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.SnapshotsApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | snapshot uid
body = wekarestapi.SnapshotsUidBody() # SnapshotsUidBody |  (optional)

try:
    # Update snapshot
    api_response = api_instance.update_snapshot(uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->update_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| snapshot uid | 
 **body** | [**SnapshotsUidBody**](SnapshotsUidBody.md)|  | [optional] 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_snapshot**
> InlineResponse20073 upload_snapshot(uid, body=body)

Upload snapshot to object store

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.SnapshotsApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | snapshot uid
body = wekarestapi.UidUploadBody() # UidUploadBody |  (optional)

try:
    # Upload snapshot to object store
    api_response = api_instance.upload_snapshot(uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->upload_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| snapshot uid | 
 **body** | [**UidUploadBody**](UidUploadBody.md)|  | [optional] 

### Return type

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

