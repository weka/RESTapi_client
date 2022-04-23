# swagger_client.ObjectStoreBucketApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_obs_bucket**](ObjectStoreBucketApi.md#create_obs_bucket) | **POST** /objectStoreBuckets | Create object store bucket
[**delete_obs_bucket**](ObjectStoreBucketApi.md#delete_obs_bucket) | **DELETE** /objectStoreBuckets/{uid} | Delete object store bucket
[**get_all_obs_buckets**](ObjectStoreBucketApi.md#get_all_obs_buckets) | **GET** /objectStoreBuckets | Get all object store buckets
[**get_obs_buckets**](ObjectStoreBucketApi.md#get_obs_buckets) | **GET** /objectStoreBuckets/{uid} | Get object store bucket
[**get_obs_operations**](ObjectStoreBucketApi.md#get_obs_operations) | **GET** /objectStoreBuckets/{uid}/operations | Get object store bucket operations
[**update_obs_bucket**](ObjectStoreBucketApi.md#update_obs_bucket) | **PUT** /objectStoreBuckets/{uid} | Update object store bucket

# **create_obs_bucket**
> InlineResponse20049 create_obs_bucket(body=body)

Create object store bucket

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreBucketApi(swagger_client.ApiClient(configuration))
body = swagger_client.ObjectStoreBucketsBody() # ObjectStoreBucketsBody |  (optional)

try:
    # Create object store bucket
    api_response = api_instance.create_obs_bucket(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreBucketApi->create_obs_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectStoreBucketsBody**](ObjectStoreBucketsBody.md)|  | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_obs_bucket**
> InlineResponse200 delete_obs_bucket(uid)

Delete object store bucket

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreBucketApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | object storage uid

try:
    # Delete object store bucket
    api_response = api_instance.delete_obs_bucket(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreBucketApi->delete_obs_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| object storage uid | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_obs_buckets**
> InlineResponse20048 get_all_obs_buckets()

Get all object store buckets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreBucketApi(swagger_client.ApiClient(configuration))

try:
    # Get all object store buckets
    api_response = api_instance.get_all_obs_buckets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreBucketApi->get_all_obs_buckets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_obs_buckets**
> InlineResponse20049 get_obs_buckets(uid)

Get object store bucket

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreBucketApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | object storage uid

try:
    # Get object store bucket
    api_response = api_instance.get_obs_buckets(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreBucketApi->get_obs_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| object storage uid | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_obs_operations**
> InlineResponse20050 get_obs_operations(uid)

Get object store bucket operations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreBucketApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | object storage uid

try:
    # Get object store bucket operations
    api_response = api_instance.get_obs_operations(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreBucketApi->get_obs_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| object storage uid | 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_obs_bucket**
> InlineResponse20049 update_obs_bucket(uid, body=body)

Update object store bucket

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreBucketApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | object storage uid
body = swagger_client.ObjectStoreBucketsUidBody() # ObjectStoreBucketsUidBody |  (optional)

try:
    # Update object store bucket
    api_response = api_instance.update_obs_bucket(uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreBucketApi->update_obs_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| object storage uid | 
 **body** | [**ObjectStoreBucketsUidBody**](ObjectStoreBucketsUidBody.md)|  | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

