# swagger_client.QuotaApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quota**](QuotaApi.md#get_quota) | **GET** /quota | Get file system quota

# **get_quota**
> InlineResponse20045 get_quota(type, fs_uid, next_token=next_token)

Get file system quota

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.QuotaApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Quota type
fs_uid = 'fs_uid_example' # str | File system uid
next_token = 'next_token_example' # str | Token to get the next page (optional)

try:
    # Get file system quota
    api_response = api_instance.get_quota(type, fs_uid, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->get_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Quota type | 
 **fs_uid** | **str**| File system uid | 
 **next_token** | **str**| Token to get the next page | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

