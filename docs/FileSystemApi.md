# swagger_client.FileSystemApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_obs_bucket_to_fs**](FileSystemApi.md#attach_obs_bucket_to_fs) | **POST** /fileSystems/{uid}/objectStoreBuckets | Attach object store bucket to file system
[**attach_obs_to_fs**](FileSystemApi.md#attach_obs_to_fs) | **POST** /fileSystems/{uid}/objectStores | Attach object store bucket to file system
[**create_file_system**](FileSystemApi.md#create_file_system) | **POST** /fileSystems | Create file system
[**delete_file_system**](FileSystemApi.md#delete_file_system) | **DELETE** /fileSystems/{uid} | Delete file system
[**delete_file_systems_thin_provision_reserve**](FileSystemApi.md#delete_file_systems_thin_provision_reserve) | **DELETE** /fileSystems/thinProvisionReserve/{org_uid} | Unset filesystems thin provisioning reserve for Organization
[**detach_obs_bucket_from_fs**](FileSystemApi.md#detach_obs_bucket_from_fs) | **DELETE** /fileSystems/{uid}/objectStoreBuckets/{obs_uid} | Detach object store bucket from file system
[**detach_obs_from_fs**](FileSystemApi.md#detach_obs_from_fs) | **DELETE** /fileSystems/{uid}/objectStores/{obs_uid} | Detach object store bucket from file system
[**download_fs**](FileSystemApi.md#download_fs) | **POST** /fileSystems/download | Download file system from object store
[**get_file_system**](FileSystemApi.md#get_file_system) | **GET** /fileSystems/{uid} | Get file system
[**get_file_systems**](FileSystemApi.md#get_file_systems) | **GET** /fileSystems | Get all file systems
[**get_file_systems_thin_provision_reserve_status**](FileSystemApi.md#get_file_systems_thin_provision_reserve_status) | **GET** /fileSystems/thinProvisionReserve | Filesystems thin provisioning reserve status for Organization
[**set_file_systems_thin_provision_reserve**](FileSystemApi.md#set_file_systems_thin_provision_reserve) | **PUT** /fileSystems/thinProvisionReserve/{org_uid} | Set filesystems thin provisioning reserve for Organization
[**update_file_system**](FileSystemApi.md#update_file_system) | **PUT** /fileSystems/{uid} | Update file system

# **attach_obs_bucket_to_fs**
> InlineResponse200 attach_obs_bucket_to_fs(body, uid)

Attach object store bucket to file system

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.UidObjectStoreBucketsBody() # UidObjectStoreBucketsBody | 
uid = 'uid_example' # str | File system uid

try:
    # Attach object store bucket to file system
    api_response = api_instance.attach_obs_bucket_to_fs(body, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->attach_obs_bucket_to_fs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UidObjectStoreBucketsBody**](UidObjectStoreBucketsBody.md)|  | 
 **uid** | **str**| File system uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_obs_to_fs**
> InlineResponse200 attach_obs_to_fs(body, uid)

Attach object store bucket to file system

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.UidObjectStoresBody() # UidObjectStoresBody | 
uid = 'uid_example' # str | File system uid

try:
    # Attach object store bucket to file system
    api_response = api_instance.attach_obs_to_fs(body, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->attach_obs_to_fs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UidObjectStoresBody**](UidObjectStoresBody.md)|  | 
 **uid** | **str**| File system uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_system**
> InlineResponse20017 create_file_system(body)

Create file system

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.FileSystemsBody() # FileSystemsBody | 

try:
    # Create file system
    api_response = api_instance.create_file_system(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->create_file_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileSystemsBody**](FileSystemsBody.md)|  | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_system**
> InlineResponse200 delete_file_system(uid, purge_from_obs=purge_from_obs)

Delete file system

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | File system uid
purge_from_obs = true # bool | Delete filesystem's objects from Object Storage, making all uploaded snapshots unusable (optional)

try:
    # Delete file system
    api_response = api_instance.delete_file_system(uid, purge_from_obs=purge_from_obs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->delete_file_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| File system uid | 
 **purge_from_obs** | **bool**| Delete filesystem&#x27;s objects from Object Storage, making all uploaded snapshots unusable | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_systems_thin_provision_reserve**
> float delete_file_systems_thin_provision_reserve(org_uid)

Unset filesystems thin provisioning reserve for Organization

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
org_uid = 'org_uid_example' # str | Organization uid for which to set reserve

try:
    # Unset filesystems thin provisioning reserve for Organization
    api_response = api_instance.delete_file_systems_thin_provision_reserve(org_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->delete_file_systems_thin_provision_reserve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_uid** | **str**| Organization uid for which to set reserve | 

### Return type

**float**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_obs_bucket_from_fs**
> InlineResponse20019 detach_obs_bucket_from_fs(uid, obs_uid)

Detach object store bucket from file system

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | file system uid
obs_uid = 'obs_uid_example' # str | object store system uid

try:
    # Detach object store bucket from file system
    api_response = api_instance.detach_obs_bucket_from_fs(uid, obs_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->detach_obs_bucket_from_fs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| file system uid | 
 **obs_uid** | **str**| object store system uid | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_obs_from_fs**
> InlineResponse20019 detach_obs_from_fs(uid, obs_uid)

Detach object store bucket from file system

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | file system uid
obs_uid = 'obs_uid_example' # str | object store system uid

try:
    # Detach object store bucket from file system
    api_response = api_instance.detach_obs_from_fs(uid, obs_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->detach_obs_from_fs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| file system uid | 
 **obs_uid** | **str**| object store system uid | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_fs**
> InlineResponse20017 download_fs(body)

Download file system from object store

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.FileSystemsDownloadBody() # FileSystemsDownloadBody | 

try:
    # Download file system from object store
    api_response = api_instance.download_fs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->download_fs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileSystemsDownloadBody**](FileSystemsDownloadBody.md)|  | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_system**
> InlineResponse20017 get_file_system(uid, force_fresh=force_fresh)

Get file system

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
uid = 'uid_example' # str | file system uid
force_fresh = true # bool | Refresh the capacities to make sure they are most updated (optional)

try:
    # Get file system
    api_response = api_instance.get_file_system(uid, force_fresh=force_fresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->get_file_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| file system uid | 
 **force_fresh** | **bool**| Refresh the capacities to make sure they are most updated | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_systems**
> InlineResponse20016 get_file_systems(force_fresh=force_fresh)

Get all file systems

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
force_fresh = true # bool | Refresh the capacities to make sure they are most updated (optional)

try:
    # Get all file systems
    api_response = api_instance.get_file_systems(force_fresh=force_fresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->get_file_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_fresh** | **bool**| Refresh the capacities to make sure they are most updated | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_systems_thin_provision_reserve_status**
> InlineResponse20018 get_file_systems_thin_provision_reserve_status()

Filesystems thin provisioning reserve status for Organization

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))

try:
    # Filesystems thin provisioning reserve status for Organization
    api_response = api_instance.get_file_systems_thin_provision_reserve_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->get_file_systems_thin_provision_reserve_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_systems_thin_provision_reserve**
> float set_file_systems_thin_provision_reserve(body, org_uid)

Set filesystems thin provisioning reserve for Organization

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.ThinProvisionReserveOrgUidBody() # ThinProvisionReserveOrgUidBody | 
org_uid = 'org_uid_example' # str | Organization uid for which to set reserve

try:
    # Set filesystems thin provisioning reserve for Organization
    api_response = api_instance.set_file_systems_thin_provision_reserve(body, org_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->set_file_systems_thin_provision_reserve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThinProvisionReserveOrgUidBody**](ThinProvisionReserveOrgUidBody.md)|  | 
 **org_uid** | **str**| Organization uid for which to set reserve | 

### Return type

**float**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_system**
> InlineResponse20017 update_file_system(body, uid)

Update file system

### Example

```python
from __future__ import print_function
import time
import wekarestapi
from wekarestapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = wekarestapi.FileSystemApi(wekarestapi.ApiClient(configuration))
body = wekarestapi.FileSystemsUidBody() # FileSystemsUidBody | 
uid = 'uid_example' # str | File system uid

try:
    # Update file system
    api_response = api_instance.update_file_system(body, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->update_file_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileSystemsUidBody**](FileSystemsUidBody.md)|  | 
 **uid** | **str**| File system uid | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

