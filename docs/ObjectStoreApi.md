# swagger_client.ObjectStoreApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_obs**](ObjectStoreApi.md#update_obs) | **PUT** /objectStores/{uid} | Update object store

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

