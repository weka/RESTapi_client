# swagger_client.MachinesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_machines**](MachinesApi.md#get_machines) | **GET** /machines | Get all machines

# **get_machines**
> InlineResponse20041 get_machines(role=role)

Get all machines

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MachinesApi(swagger_client.ApiClient(configuration))
role = ['role_example'] # list[str] |  (optional)

try:
    # Get all machines
    api_response = api_instance.get_machines(role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachinesApi->get_machines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

