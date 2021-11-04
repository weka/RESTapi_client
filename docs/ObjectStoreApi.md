# swagger_client.ObjectStoreApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_obs**](ObjectStoreApi.md#create_obs) | **POST** /objectStores | Create object store
[**delete_obs**](ObjectStoreApi.md#delete_obs) | **DELETE** /objectStores/{uid} | Delete object store
[**get_all_obs**](ObjectStoreApi.md#get_all_obs) | **GET** /objectStores | Get all object stores
[**get_obs**](ObjectStoreApi.md#get_obs) | **GET** /objectStores/{uid} | Get object store
[**update_obs**](ObjectStoreApi.md#update_obs) | **PUT** /objectStores/{uid} | Update object store

# **create_obs**
> InlineResponse200 create_obs(body=body)

Create object store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.ObjectStoresBody() # ObjectStoresBody |  (optional)

try:
    # Create object store
    api_response = api_instance.create_obs(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreApi->create_obs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ObjectStoresBody**](ObjectStoresBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_obs**
> InlineResponse200 delete_obs(uid)

Delete object store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | object storage uid

try:
    # Delete object store
    api_response = api_instance.delete_obs(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreApi->delete_obs: %s\n" % e)
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

# **get_all_obs**
> InlineResponse20040 get_all_obs()

Get all object stores

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreApi(swagger_client.ApiClient(configuration))

try:
    # Get all object stores
    api_response = api_instance.get_all_obs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreApi->get_all_obs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_obs**
> InlineResponse20041 get_obs(uid)

Get object store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | object storage uid

try:
    # Get object store
    api_response = api_instance.get_obs(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreApi->get_obs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| object storage uid | 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_obs**
> InlineResponse200 update_obs(uid, body=body)

Update object store

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ObjectStoreApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | object storage uid
body = swagger_client.ObjectStoresUidBody() # ObjectStoresUidBody |  (optional)

try:
    # Update object store
    api_response = api_instance.update_obs(uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectStoreApi->update_obs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| object storage uid | 
 **body** | [**ObjectStoresUidBody**](ObjectStoresUidBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

